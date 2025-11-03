import tkinter as tk

root = tk.Tk()
root.title("GUI Square Grid")
root.geometry("300x300")

frame1 = tk.Frame(root, bd=5, relief="groove")
frame2 = tk.Frame(root, bd=5, relief="groove")
frame1.pack(side="left", anchor="w", fill="both", expand="1")
frame2.pack(side="right", anchor="e", fill="both", expand="1")

tk.Label(frame1, text="A", fg="white", bg="#212F58").pack(side="top", anchor="n", fill="both", expand="1")
tk.Label(frame1, text="B").pack(side="bottom", anchor="s", fill="both", expand="1")
tk.Label(frame2, text="C").pack(side="top", anchor="n", fill="both", expand="1")
tk.Label(frame2, text="D", fg="white", bg="#212F58").pack(side="bottom", anchor="s", fill="both", expand="1")

root.mainloop()