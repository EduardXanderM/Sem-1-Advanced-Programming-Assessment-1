import tkinter as tk

root = tk.Tk()
root.title("GUI Login Page")
root.geometry("300x170")
root.config(background="#ebebeb")
root.resizable(width=False, height=False)

tk.Label(root, text="Username:", width=15).grid(column=0, row=0, padx=2, pady=6)
tk.Entry(root, width=25).grid(column=1, row=0)
tk.Label(root, text="Password:", width=15).grid(column=0, row=1, padx=2, pady=6)
tk.Entry(root, width=25).grid(column=1, row=1)
tk.Checkbutton(root, text="Remember me", width=15, anchor="e").grid(column=0, row=2, columnspan=2, padx=16, pady=6, sticky="w")
tk.Button(root, text="Login", padx=4, pady=2).grid(column=0, row=3, columnspan=2, padx=2, pady=6, sticky="n")


root.mainloop()