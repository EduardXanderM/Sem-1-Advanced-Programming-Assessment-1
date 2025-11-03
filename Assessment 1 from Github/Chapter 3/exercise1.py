import tkinter as tk

def update_greeting():
    name = name_entry.get().strip()
    color = color_var.get()
    if name:
        greeting_label.config(text=f"Hello, {name}!", fg=color)
    else:
        greeting_label.config(text="Please enter your name.", fg="black")

root = tk.Tk()
root.title("Greeting App")
root.geometry("400x300")

input_frame = tk.Frame(root, bg="#82B4C7", padx=10, pady=10)
input_frame.pack(fill="x")

title_label = tk.Label(input_frame, text="Greeting App", font=("Times New Roman", 16, "bold"), fg="blue", bg="#82B4C7")
title_label.pack(pady=5)

tk.Label(input_frame, text="Enter your name:", bg="#82B4C7", font=("Times New Roman", 11)).pack()
name_entry = tk.Entry(input_frame, width=25)
name_entry.pack(pady=5)

tk.Label(input_frame, text="Select color:", bg="#82B4C7", font=("Times New Roman", 11)).pack()

color_var = tk.StringVar(value="black")
color_options = ["red", "green", "blue", "purple", "orange", "black"]
color_menu = tk.OptionMenu(input_frame, color_var, *color_options)
color_menu.pack(pady=5)

update_button = tk.Button(input_frame, text="Update Greeting", command=update_greeting, font=("Times New Roman", 11), relief="raised", bd=2)
update_button.pack(pady=10)

display_frame = tk.Frame(root, bg="#6BB37B", height=100)
display_frame.pack(fill="both", expand=True)

greeting_label = tk.Label(display_frame, text="", font=("Arial", 14), bg="#6BB37B")
greeting_label.pack(pady=20)

# Run app
root.mainloop()
