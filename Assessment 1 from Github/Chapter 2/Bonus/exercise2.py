import tkinter as tk
from tkinter import messagebox
from datetime import date

def calculate_age():
    dob_input = dob_entry.get().strip()
    if not dob_input:
        messagebox.showerror("Error", "Please enter the date of your birth...")
        return
    try:
        day, month, year = map(int, dob_input.split("/"))
        dob = date(year, month, day)
        today = date.today()
        age = today.year - dob.year
        if (today.month, today.day) < (dob.month, dob.day):
            age -= 1
        result_label.config(text=f"Your age is {age}. Congratulations!")
    except ValueError:
        messagebox.showerror("Error", "Please enter a valid date in the format dd/mm/yyyy format to proceed...")

root = tk.Tk()
root.title("Age Calculator")
root.geometry("350x200")
root.config(bg="#8F374D")

tk.Label(root, text="Age Calculator", font=("Times New Roman", 16, "bold"), fg="#2F0510", bg="#8F374D").pack(pady=10)

tk.Label(root, text="Enter your date of birth (dd/mm/yyyy):", bg="#8F374D", font=("Times New Roman", 11, "bold")).pack()
dob_entry = tk.Entry(root, width=20)
dob_entry.pack(pady=5)

tk.Button(root, text="Calculate Age", command=calculate_age, bg="#3E0916", fg="white", font=("Times New Roman", 12, "bold")).pack(pady=10)

result_label = tk.Label(root, text="", font=("Arial", 12), bg="#8F374D")
result_label.pack(pady=5)

root.mainloop()
