import tkinter as tk
from tkinter import messagebox

def draw_shape():
    canvas.delete("all")
    shape = shape_var.get()

    try:
        x1 = int(x1_entry.get())
        y1 = int(y1_entry.get())
        x2 = int(x2_entry.get())
        y2 = int(y2_entry.get())
    except ValueError:
        messagebox.showerror("Error", "Please enter valid integer coordinates.")
        return

    if shape == "Oval":
        canvas.create_oval(x1, y1, x2, y2, fill="lightblue", outline="blue", width=2)
    elif shape == "Rectangle":
        canvas.create_rectangle(x1, y1, x2, y2, fill="lightgreen", outline="green", width=2)
    elif shape == "Square":
        side = min(x2 - x1, y2 - y1)
        canvas.create_rectangle(x1, y1, x1 + side, y1 + side, fill="orange", outline="darkorange", width=2)
    elif shape == "Triangle":
        canvas.create_polygon(x1, y2, (x1+x2)//2, y1, x2, y2, fill="pink", outline="red", width=2)
    else:
        messagebox.showwarning("Warning", "Please select a shape first.")

root = tk.Tk()
root.title("Shape Drawer (With Coordinates Extension)")
root.geometry("450x500")
root.config(bg="#9C666A")
root.resizable(width=False, height=False)

shape_var = tk.StringVar(value="")

tk.Label(root, text="Select a Shape:", font=("Arial", 12, "bold"), bg="#9C666A").pack(pady=5)
for s in ["Oval", "Rectangle", "Square", "Triangle"]:
    tk.Radiobutton(root, text=s, variable=shape_var, value=s, bg="#9C666A").pack(anchor="w", padx=140)

coord_frame = tk.Frame(root, bg="#9C666A")
coord_frame.pack(pady=10)
tk.Label(coord_frame, text="x1:", bg="#9C666A").grid(row=0, column=0)
x1_entry = tk.Entry(coord_frame, width=5)
x1_entry.grid(row=0, column=1)
tk.Label(coord_frame, text="y1:", bg="#9C666A").grid(row=0, column=2)
y1_entry = tk.Entry(coord_frame, width=5)
y1_entry.grid(row=0, column=3)
tk.Label(coord_frame, text="x2:", bg="#9C666A").grid(row=0, column=4)
x2_entry = tk.Entry(coord_frame, width=5)
x2_entry.grid(row=0, column=5)
tk.Label(coord_frame, text="y2:", bg="#9C666A").grid(row=0, column=6)
y2_entry = tk.Entry(coord_frame, width=5)
y2_entry.grid(row=0, column=7)

tk.Button(root, text="Draw Shape", command=draw_shape, bg="#571E22", fg="white", font=("Arial", 10, "bold")).pack(pady=10)

canvas = tk.Canvas(root, width=350, height=250, bg="white", relief="sunken", borderwidth=2)
canvas.pack(pady=10)

root.mainloop()
