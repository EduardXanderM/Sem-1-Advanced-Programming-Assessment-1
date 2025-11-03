import tkinter as tk
from tkinter import font

window = tk.Tk()
window.title("Welcome Window")
window.geometry("300x200")
window.resizable(False, False)
window.config(bg="#b3e5fc") 
custom_font = ("Helvetica", 18, "bold")
label = tk.Label(window, text="Welcome to Tkinter!", font=custom_font, bg="#b3e5fc", fg="#003366")
label.pack(expand=True)

window.mainloop()