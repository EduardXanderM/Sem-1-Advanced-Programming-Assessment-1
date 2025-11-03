import tkinter as tk
from tkinter import *
from tkinter import ttk
from PIL import Image, ImageTk

root = tk.Tk()
root.title("GUI Login Page")
root.geometry("400x750")
root.config(background="#ffffff")
root.resizable(width=False, height=False)

original_logo = Image.open("Assessment 1 from Github/Chapter 2/bsu.jpeg")
new_width = 400
new_height = 95
resized_image = original_logo.resize((new_width, new_height), Image.Resampling.LANCZOS)
tk_logo = ImageTk.PhotoImage(resized_image)

tk.Label(root, image=tk_logo).pack(anchor="nw", side="top")

main_frame = tk.Frame(root, bg="#e3e3e3", width=350)
main_frame.pack(fill="both", expand=True, pady=5, padx=20)

tk.Label(main_frame, text="Student Management System", bg="#e3e3e3", font=("Arial", 16, "bold")).pack(anchor="center", side="top", pady=5)
tk.Label(main_frame, text="New Student Registration", bg="#e3e3e3", font=("Arial", 13, "bold")).pack(anchor="center", side="top")

registration_frame = tk.Frame(main_frame, bg="#e3e3e3")
registration_frame.pack(fill="x", expand=True, side="top", anchor="n", pady=10)

genders = ["Male", "Female", "Would not like to say"]
opt = StringVar(value="Would not like to say")

tk.Label(registration_frame, text="Student Name", bg="#e3e3e3", font=("Arial", 11)).grid(row=0, column=0, padx=4)
tk.Entry(registration_frame, width=18, relief="ridge", bd=2, font=("Arial", 14)).grid(row=0, column=1, columnspan=2, sticky="e", pady=6)

tk.Label(registration_frame, text="Mobile Number", bg="#e3e3e3", font=("Arial", 11)).grid(row=1, column=0)
tk.Entry(registration_frame, width=18, relief="ridge", bd=2, font=("Arial", 14)).grid(row=1, column=1, columnspan=2, sticky="e", pady=6)

tk.Label(registration_frame, text="Email ID", bg="#e3e3e3", font=("Arial", 11)).grid(row=2, column=0)
tk.Entry(registration_frame, width=18, relief="ridge", bd=2, font=("Arial", 14)).grid(row=2, column=1, columnspan=2, sticky="e", pady=6)

tk.Label(registration_frame, text="Home Address", bg="#e3e3e3", font=("Arial", 11)).grid(row=3, column=0)
tk.Entry(registration_frame, width=18, relief="ridge", bd=2, font=("Arial", 14)).grid(row=3, column=1, columnspan=2, sticky="e", pady=6)

tk.Label(registration_frame, text="Gender", bg="#e3e3e3", font=("Arial", 11)).grid(row=4, column=0)
gender_menu = tk.OptionMenu(registration_frame, opt, *genders)
gender_menu.config(font=("Arial", 12), relief="ridge",bd=2)
gender_menu.grid(row=4, column=1, columnspan=2, pady=6)

tk.Label(registration_frame, text="Course Enrolled", bg="#e3e3e3", font=("Arial", 11)).grid(row=5, column=0, padx=4)
tk.Radiobutton(registration_frame, text="BSc CC", bg="#e3e3e3", font=("Arial", 11), value=1).grid(row=5, column=1, pady=3)
tk.Radiobutton(registration_frame, text="BSc CY", bg="#e3e3e3", font=("Arial", 11), value=2).grid(row=6, column=1, pady=3)
tk.Radiobutton(registration_frame, text="BsC PSY", bg="#e3e3e3", font=("Arial", 11), value=3).grid(row=7, column=1, pady=3)
tk.Radiobutton(registration_frame, text="BA & BM", bg="#e3e3e3", font=("Arial", 11), value=4).grid(row=8, column=1, pady=3)

tk.Label(registration_frame, text="Languages Known", bg="#e3e3e3", font=("Arial", 11)).grid(row=9, column=0, padx=4)
tk.Checkbutton(registration_frame, text="English", bg="#e3e3e3", font=("Arial", 11)).grid(row=9, column=1)
tk.Checkbutton(registration_frame, text="Tagalog", bg="#e3e3e3", font=("Arial", 11)).grid(row=9, column=2, pady=3)
tk.Checkbutton(registration_frame, text="Hindi/Urdu", bg="#e3e3e3", font=("Arial", 11)).grid(row=10, column=1, pady=3)

tk.Label(registration_frame, text="Rate your English communication skills", bg="#e3e3e3", font=("Arial", 11, "bold")).grid(row=11, column=0, columnspan=3, pady=6, padx=8)

ttk.Scale(registration_frame, orient=HORIZONTAL, from_=0, to=100).grid(row=12, column=0, columnspan=3, sticky="we", padx=40)

tk.Button(main_frame, text="Submit", relief="solid", bg="#22263d", fg="white", font=("Arial", 13), width=14, height=2).pack(side="left", anchor="w", padx=15, pady=15)
tk.Button(main_frame, text="Clear", relief="solid", bg="#22263d", fg="white", font=("Arial", 13), width=14, height=2).pack(side="right", anchor="e", padx=15, pady=15)

root.mainloop()