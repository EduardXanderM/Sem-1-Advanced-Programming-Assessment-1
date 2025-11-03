import tkinter as tk
from tkinter import messagebox

def calculate():
    celsius = celsius_entry.get()
    fahrenheit = fahrenheit_entry.get()
    if celsius and fahrenheit:
        messagebox.showerror("Error", "Please fill only one field, not both...")
        return
    elif not celsius and not fahrenheit:
        messagebox.showerror("Error", "Please enter either celsius or fahrenheit to convert...")
        return
    try:
        if celsius:
            c = float(celsius)
            f = (c * 9/5) + 32
            fahrenheit_entry.delete(0, tk.END)
            fahrenheit_entry.insert(0, f"{f:.2f}")
        else:
            f = float(fahrenheit)
            c = (f - 32) * 5/9
            celsius_entry.delete(0, tk.END)
            celsius_entry.insert(0, f"{c:.2f}")
    except ValueError:
        messagebox.showerror("Error", "Please enter a valid number...")

root = tk.Tk()
root.title("Celsius and Fahrenheit Converter")
root.geometry("230x150")
root.config(bg="#E8F8F5")

tk.Label(root, text="Celsius:", bg="#E8F8F5", font=("Calibri", 11)).grid(row=0, column=0, padx=10, pady=10)
celsius_entry = tk.Entry(root, width=15)
celsius_entry.grid(row=0, column=1, padx=10, pady=10)

tk.Label(root, text="Fahrenheit:", bg="#E8F8F5", font=("Calibri", 11)).grid(row=1, column=0, padx=10, pady=10)
fahrenheit_entry = tk.Entry(root, width=15)
fahrenheit_entry.grid(row=1, column=1, padx=10, pady=10)

calc_button = tk.Button(root, text="Calculate", command=calculate, bg="#45B39D", fg="white", font=("Calibri", 11, "bold"), padx=3, pady=2)
calc_button.grid(row=2, column=0, columnspan=2, pady=10)

root.mainloop()