# Мой первый проект
# писал на ткинтере (о господи какая неаЖИДоность)

import tkinter
import random

root = tkinter.Tk()
root.title("Кликер")
root.geometry("512x512")

money = 1000
x_count = 0
x_int_price = 1000

click_button = tkinter.Button(text="Клик")
click_button.place(x = 206, y = 400, width=100, height=50)

balance = tkinter.Label(text="Баланс: " + str(money))
balance.pack(side="top")

x_upgrade = tkinter.Button(text="+0.1 к клику")
x_upgrade.pack(expand=True)

x_price = tkinter.Label(text="Цена: " + str(x_int_price))
x_price.place(x = 225, y = 230)

def click(event):
    global money
    global x_count
    if x_count == 0:
        money = money + 1
        balance.configure(text="Баланс: " + str(money))
        print(money)
    if x_count > 1:
        money = money + 1 * x_count
        balance.configure(text="Баланс: " + str(money))
        print(money)

click_button.bind("<Button>", click)

def buy(event):
    global money
    global x_count
    global x_int_price
    if money >= x_int_price:
        money = money - x_int_price
        x_int_price = x_int_price + 500
        x_price.configure(text="Цена: " + str(x_int_price))
        balance.configure(text="Баланс: " + str(round(money)))
        x_count += 1.10
    if money < x_int_price:
        print("net deneg))")

x_upgrade.bind("<Button>", buy)


root.mainloop()
