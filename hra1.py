import pygame
import sys

# Inicializace Pygame
pygame.init()

# Nastavení velikosti okna
screen_width = 800
screen_height = 600
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Základní program v Pygame")

# Definice barev
WHITE = (255, 255, 255)
BLUE = (0, 0, 255)

# Inicializace čtverce
square_size = 50
square_x = screen_width // 2 - square_size // 2
square_y = screen_height // 2 - square_size // 2
square_speed = 5

# Hlavní smyčka programu
running = True
while running:
    # Kontrola událostí
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Klávesy pro pohyb
    keys = pygame.key.get_pressed()
    
    if keys[pygame.K_LEFT]:
        square_x -= square_speed
    if keys[pygame.K_RIGHT]:
        square_x += square_speed
    if keys[pygame.K_UP]:
        square_y -= square_speed
    if keys[pygame.K_DOWN]:
        square_y += square_speed

    # Vyplnění pozadí
    screen.fill(WHITE)

    # Vykreslení čtverce
    pygame.draw.rect(screen, BLUE, (square_x, square_y, square_size, square_size))

    # Aktualizace displeje
    pygame.display.flip()

    # Omezení FPS
    pygame.time.Clock().tick(30)

# Ukončení programu
pygame.quit()
sys.exit()
