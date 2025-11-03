import tkinter as tk
from tkinter import ttk, messagebox
import math

def area_circle():
    try:
        r = float(radius_entry.get())
        area = math.pi * r ** 2
        messagebox.showinfo("Circle Area", f"Area of Circle: {area:.2f}")
    except ValueError:
        messagebox.showerror("Error", "Please enter a valid number for radius.")

def area_square():
    try:
        side = float(side_entry.get())
        area = side ** 2
        messagebox.showinfo("Square Area", f"Area of Square: {area:.2f}")
    except ValueError:
        messagebox.showerror("Error", "Please enter a valid number for side length.")

def area_rectangle():
    try:
        length = float(length_entry.get())
        width = float(width_entry.get())
        area = length * width
        messagebox.showinfo("Rectangle Area", f"Area of Rectangle: {area:.2f}")
    except ValueError:
        messagebox.showerror("Error", "Please enter valid numbers for length and width.")

root = tk.Tk()
root.title("Area Calculator")
root.geometry("300x250")
root.config(bg="#827265")
root.resizable(width=False, height=False)

notebook = ttk.Notebook(root)
notebook.pack(expand=True, fill="both", padx=10, pady=10)

circle_tab = ttk.Frame(notebook)
notebook.add(circle_tab, text="Circle")

tk.Label(circle_tab, text="Enter Radius:", font=("Arial", 11)).pack(pady=10)
radius_entry = tk.Entry(circle_tab)
radius_entry.pack(pady=5)
tk.Button(circle_tab, text="Calculate Area", command=area_circle, bg="#4541B7", fg="white").pack(pady=10)

square_tab = ttk.Frame(notebook)
notebook.add(square_tab, text="Square")

tk.Label(square_tab, text="Enter Side Length:", font=("Arial", 11)).pack(pady=10)
side_entry = tk.Entry(square_tab)
side_entry.pack(pady=5)
tk.Button(square_tab, text="Calculate Area", command=area_square, bg="#21A16C", fg="white").pack(pady=10)

rectangle_tab = ttk.Frame(notebook)
notebook.add(rectangle_tab, text="Rectangle")

tk.Label(rectangle_tab, text="Enter Length:", font=("Arial", 11)).pack(pady=5)
length_entry = tk.Entry(rectangle_tab)
length_entry.pack(pady=5)

tk.Label(rectangle_tab, text="Enter Width:", font=("Arial", 11)).pack(pady=5)
width_entry = tk.Entry(rectangle_tab)
width_entry.pack(pady=5)

tk.Button(rectangle_tab, text="Calculate Area", command=area_rectangle, bg="#D3873B", fg="white").pack(pady=10)

root.mainloop()
