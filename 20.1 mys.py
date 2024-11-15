import tkinter as tk

# Vytvoření hlavního okna
root = tk.Tk()
root.title("Kreslení s myší")

# Vytvoření plátna
canvas = tk.Canvas(root, width=400, height=400, bg='white')
canvas.pack()

# Funkce pro zpracování události myši
def klik(mys):
    print(mys.x, mys.y)  # Vypíše souřadnice myši do konzole
    # Kreslení tečky na plátno na pozici myši
    canvas.create_oval(mys.x-1, mys.y-1, mys.x+1, mys.y+1, fill='black')

# Bind pro levé tlačítko myši a tažení
canvas.bind('<B1-Motion>', klik)

# Spuštění hlavní událostní smyčky Tkinteru
root.mainloop()
