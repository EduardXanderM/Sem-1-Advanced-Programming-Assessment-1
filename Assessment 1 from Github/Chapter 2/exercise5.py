import tkinter as tk
from tkinter import messagebox

def calculate(operation):
    try:
        num1 = float(entry1.get().strip())
        num2 = float(entry2.get().strip())
        if operation == "+":
            result = num1 + num2
        elif operation == "-":
            result = num1 - num2
        elif operation == "*":
            result = num1 * num2
        elif operation == "/":
            if num2 == 0:
                messagebox.showerror("Error", "Division by zero is not allowed")
                return
            result = num1 / num2
        elif operation == "%":
            result = num1 % num2
        label_result.config(text=f"Result: {result}")
    except ValueError:
        messagebox.showerror("Error", "Please enter valid numbers")

root = tk.Tk()
root.title("Calculator")
root.geometry("300x300")
root.config(background="#a2cbd2")
root.resizable(width=False, height=False)

tk.Label(root, text="Enter first number:", bg="#a2cbd2", font=("Comic Sans", 12)).pack(pady=5)
entry1 = tk.Entry(root)
entry1.pack(pady=5)

tk.Label(root, text="Enter second number:", bg="#a2cbd2", font=("Comic Sans", 12)).pack(pady=5)
entry2 = tk.Entry(root)
entry2.pack(pady=5)

button_frame = tk.Frame(root, bg="#a2cbd2")
button_frame.pack(pady=10)

tk.Button(button_frame, text="+", width=5, command=lambda: calculate("+"), font=("Comic Sans", 12)).grid(row=0, column=0, padx=5, pady=5)
tk.Button(button_frame, text="-", width=5, command=lambda: calculate("-"), font=("Comic Sans", 12)).grid(row=0, column=1, padx=5, pady=5)
tk.Button(button_frame, text="*", width=5, command=lambda: calculate("*"), font=("Comic Sans", 12)).grid(row=0, column=2, padx=5, pady=5)
tk.Button(button_frame, text="/", width=5, command=lambda: calculate("/"), font=("Comic Sans", 12)).grid(row=1, column=0, padx=5, pady=5)
tk.Button(button_frame, text="%", width=5, command=lambda: calculate("%"), font=("Comic Sans", 12)).grid(row=1, column=1, padx=5, pady=5)

label_result = tk.Label(root, text="Result: ", bg="#a2cbd2", font=("Comic Sans", 12))
label_result.pack(pady=20)

root.mainloop()