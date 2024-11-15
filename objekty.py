spolecne_score = 1


class Osoba:
    def __init__(self, jmeno, vek):
        self.jmeno = jmeno
        self.vek = vek

    def predstav_se(self):
        global spolecne_score
        spolecne_score = 5
        tmp = 2 + 2
        self.vek = tmp
        return f"Ahoj, jmenuji se {self.jmeno} a je mi {self.vek} let."

    def oslav_narozeniny(self):
        self.vek += 1
        return f"Všechno nejlepší! Nyní je ti {self.vek} let."


# Vytvoření seznamu osob
osoby = [
    Osoba("Petr", 25),
    Osoba("Eva", 30),
    Osoba("Jan", 22),
    Osoba("Anna", 28)
]

print(osoby[2].vek)
print(osoby[3].predstav_se())
print(spolecne_score)

# Výpis informací o každé osobě
# for osoba in osoby:
#    print(osoba.predstav_se())
