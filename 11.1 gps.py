import tkinter as tk
import random

def gps():
    x = random.randint(0, 400)
    y = random.randint(0, 400)
    canvas.create_text(x, y, text='+', font=("Arial", 24), fill="red")
    canvas.create_text(x, y+20, text=f'({x}, {y})', font=("Arial", 12), fill="blue")

def run_gps():
    for _ in range(10):
        gps()

# Create the main window
root = tk.Tk()
root.title("GPS Tracker")

# Create a canvas
canvas = tk.Canvas(root, width=400, height=400, bg='white')
canvas.pack()

# Run the GPS simulation
run_gps()

# Start the Tkinter event loop
root.mainloop()
