import tkinter as tk

root = tk.Tk()  # Create the main window
canvas = tk.Canvas(root, width=300, height=200)  # Create a canvas with a specified size
canvas.pack()  # Pack the canvas into the window
canvas.create_rectangle(50, 70, 220, 150)  # Create a rectangle on the canvas
canvas.create_rectangle(20, 20, 50, 50)
root.mainloop()  # Start the Tkinter main loop

