import tkinter as tk
from tkinter import messagebox
from PIL import Image, ImageTk

prices = {
    "Espresso": 5,
    "Cappuccino": 7,
    "Latte": 6,
    "Americano": 4,
    "Frappuccino": 9
}

def make_coffee():
    coffee = coffee_var.get()
    sugar = sugar_var.get()
    milk = milk_var.get()
    honey = honey_var.get()
    cinnamon = cinnamon_var
    paid = float(money_entry.get() or 0)
    cost = prices[coffee]

    if paid < cost:
        messagebox.showerror("Payment Error", f"{coffee} costs {cost} AED. You only paid {paid} AED.")
    else:
        change = paid - cost
        message = f"You selected {coffee} with "
        message += "sugar, " if sugar else "no sugar, "
        message += "milk, " if milk else "no milk, "
        message += "honey, " if honey else "no honey, "
        message += "cinnamon." if cinnamon else "no cinnamon."
        message += f"\nPayment accepted! Change: {change:.2f} AED."
        messagebox.showinfo("Order Confirmed", message)

root = tk.Tk()
root.title("Coffee Vending Machine")
root.geometry("400x500")
root.config(bg="#D79377")

try:
    coffee_img = Image.open("Assessment 1 from Github/Chapter 3/coffee.png")
    coffee_img = coffee_img.resize((250, 150))
    coffee_photo = ImageTk.PhotoImage(coffee_img)
    tk.Label(root, image=coffee_photo, bg="#D79377").pack(pady=10)
except:
    tk.Label(root, text="[Coffee Image Missing]", bg="#E6BEAE", font=("Arial", 10, "italic")).pack(pady=10)

tk.Label(root, text="Select Coffee Type:", font=("Arial", 12, "bold"), bg="#D79377").pack()
coffee_var = tk.StringVar(value="Espresso")
tk.OptionMenu(root, coffee_var, *prices.keys()).pack(pady=5)

sugar_var = tk.BooleanVar()
tk.Checkbutton(root, text="Add Sugar", variable=sugar_var, bg="#D79377").pack()

milk_var = tk.BooleanVar()
tk.Checkbutton(root, text="Add Milk", variable=milk_var, bg="#D79377").pack()

honey_var = tk.BooleanVar()
tk.Checkbutton(root, text="Add Honey", variable=honey_var, bg="#D79377").pack()

cinnamon_var = tk.BooleanVar()
tk.Checkbutton(root, text="Add Cinammon", variable=cinnamon_var, bg="#D79377").pack()

tk.Label(root, text="Insert Money (AED):", bg="#D79377").pack(pady=5)
money_entry = tk.Entry(root)
money_entry.pack(pady=5)

tk.Button(root, text="Make Coffee", command=make_coffee, bg="#A0522D", fg="white", width=15).pack(pady=20)

root.mainloop()
