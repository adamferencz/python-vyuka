import pygame
import serial  # type: ignore
import time
import math
import random

# Inicializace pygame
pygame.init()
screen = pygame.display.set_mode((800, 600))
pygame.display.set_caption("Micro:bit Multiplayer Game")

# Barvy
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
GREEN = (0, 255, 0)

# Inicializace sériového portu
ser = serial.Serial("COM6", 115200, timeout=1)
time.sleep(2)  # Pauza pro inicializaci spojení


# Třída pro hráče
class Player:
    def __init__(self, name, x, y):
        self.name = name
        self.x = x
        self.y = y
        self.color = (
            random.randint(50, 255),
            random.randint(50, 255),
            random.randint(50, 255)
        )
        self.radius = 20
        self.speed = 5
        self.angle = random.randint(0, 360)  # Náhodný výchozí směr

    def update_position(self):
        self.x += self.speed * math.cos(math.radians(self.angle))
        self.y += self.speed * math.sin(math.radians(self.angle))
        self.x %= 800  # Cyklické ohraničení horizontálně
        self.y %= 600  # Cyklické ohraničení vertikálně

    def draw(self, surface):
        pygame.draw.circle(surface, self.color, (int(self.x), int(self.y)), self.radius)
        font = pygame.font.SysFont(None, 20)
        name_text = font.render(self.name, True, BLACK)
        surface.blit(name_text, (self.x - self.radius, self.y - self.radius - 10))


# Třída pro jídlo
class Food:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.color = RED
        self.radius = 10

    def draw(self, surface):
        pygame.draw.circle(surface, self.color, (int(self.x), int(self.y)), self.radius)


# Seznam hráčů a jídla
players = {}
food_items = []

# Funkce pro generování jídla
def spawn_food():
    x = random.randint(20, 780)
    y = random.randint(20, 580)
    food_items.append(Food(x, y))

# Funkce pro kontrolu kolizí
def check_collisions():
    global players, food_items

    for player_id, player in list(players.items()):
        # Kontrola kolize hráče s jídlem
        for food in food_items[:]:
            distance = math.sqrt((player.x - food.x) ** 2 + (player.y - food.y) ** 2)
            if distance < player.radius + food.radius:
                player.radius += 2  # Hráč se zvětší
                food_items.remove(food)

        # Kontrola kolize hráče s jinými hráči
        for other_id, other_player in list(players.items()):
            if player_id == other_id:
                continue
            distance = math.sqrt((player.x - other_player.x) ** 2 + (player.y - other_player.y) ** 2)
            if distance < player.radius + other_player.radius:
                if player.radius > other_player.radius:  # Větší hráč sní menšího
                    player.radius += int(other_player.radius / 2)
                    del players[other_id]

# Funkce pro zobrazení vítězné obrazovky
def show_winner(winner):
    screen.fill(WHITE)
    font = pygame.font.SysFont(None, 50)
    text = font.render(f"Congratulations {winner.name}! You win!", True, GREEN)
    screen.blit(text, (400 - text.get_width() // 2, 300 - text.get_height() // 2))
    pygame.display.flip()
    time.sleep(5)  # Pauza 5 sekund
    reset_game()

# Funkce pro reset hry
def reset_game():
    global players, food_items
    players = {}
    food_items = []
    for _ in range(10):  # Znovu vygeneruj jídlo
        spawn_food()

# Hlavní smyčka hry
running = True
spawn_timer = 0
while running:
    screen.fill(WHITE)

    # Čtení dat ze sériového portu
    if ser.in_waiting > 0:
        microbitdata = ser.readline().decode().strip()
        print(microbitdata)

        # Zpracování zpráv s formátem ID:left nebo ID:right
        try:
            device_id, command = microbitdata.split(':')

            # Přidání hráče, pokud ještě neexistuje
            if device_id not in players:
                players[device_id] = Player(device_id, random.randint(100, 700), random.randint(100, 500))

            # Úprava směru hráče podle příkazu
            if command == "0":
                players[device_id].angle -= 45  # Doleva
            elif command == "1":
                players[device_id].angle += 45  # Doprava
        except ValueError:
            print("Nesprávný formát zprávy")

    # Aktualizace a vykreslení hráčů
    for player in players.values():
        player.update_position()
        player.draw(screen)
        if player.radius > 100:  # Kontrola výhry
            show_winner(player)

    # Aktualizace a vykreslení jídla
    for food in food_items:
        food.draw(screen)

    # Kontrola kolizí
    check_collisions()

    # Spawn nového jídla každých 100 cyklů
    spawn_timer += 1
    if spawn_timer >= 100:
        spawn_food()
        spawn_timer = 0

    pygame.display.flip()

    # Kontrola zavření okna
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    pygame.time.delay(30)  # Aktualizace každých 30 ms

# Ukončení
ser.close()
pygame.quit()
