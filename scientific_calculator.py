import tkinter as tk
import math

root = tk.Tk()
root.title("Scientific Calculator")
root.geometry("470x650")


display = tk.Entry(
    root,
    font=("Arial", 30),
    justify="right",
    width=20,
    bd=5
)

display.grid(row=0, column=0, columnspan=5, padx=10, pady=(20,10), ipady=15)

message = tk.Label(
    root,
    text="",
    fg="red",
    font=("Arial",12)
)

message.grid(row=1,column=0,columnspan=5)

def click(value):
    display.insert(tk.END, value)
    message.config(text="")

def clear():
    display.delete(0, tk.END)
    message.config(text="")

def backspace():
    if display.get():
        display.delete(len(display.get())-1)

def equal(event=None):
    try:
        expression = display.get().replace("%","/100")
        result = eval(expression)

        display.delete(0, tk.END)
        display.insert(0, result)

        message.config(text="")

    except:
        message.config(text="Invalid Input")

def square_root():
    try:
        number = float(display.get())

        result = math.sqrt(number)

        display.delete(0, tk.END)
        display.insert(0, result)

        message.config(text="")

    except:
        message.config(text="Invalid Input")

def square():
    try:
        number = float(display.get())

        result = number ** 2

        display.delete(0, tk.END)
        display.insert(0, result)

        message.config(text="")

    except:
        message.config(text="Invalid Input")

def logarithm():
    try:
        number = float(display.get())

        result = math.log10(number)

        display.delete(0, tk.END)
        display.insert(0, result)

        message.config(text="")

    except:
        message.config(text="Invalid Input")

def natural_log():
    try:
        number = float(display.get())

        result = math.log(number)

        display.delete(0, tk.END)
        display.insert(0, result)

        message.config(text="")

    except:
        message.config(text="Invalid Input")

def key_pressed(event):

    key = event.char

    allowed = "0123456789+-*/().%"

    if key in allowed:
        click(key)

root.bind("<Return>", equal)
root.bind("<BackSpace>", lambda event: backspace())
root.bind("<Key>", key_pressed)

buttons = [
    ("(",2,0),
    (")",2,1),
    ("√",2,2),
    ("x²",2,3),
    ("C",2,4),

    ("log",3,0),
    ("ln",3,1),
    ("%",3,2),
    ("/",3,3),
    ("*",3,4),

    ("7",4,0),
    ("8",4,1),
    ("9",4,2),
    ("-",4,3),

    ("4",5,0),
    ("5",5,1),
    ("6",5,2),
    ("+",5,3),

    ("1",6,0),
    ("2",6,1),
    ("3",6,2),

    ("0",7,0),
    (".",7,2),
    ("⌫",7,3)
]

for text,row,column in buttons:

    if text == "C":
        command = clear

    elif text == "√":
        command = square_root

    elif text == "x²":
        command = square

    elif text == "log":
        command = logarithm

    elif text == "ln":
        command = natural_log

    elif text == "⌫":
        command = backspace

    else:
        command = lambda t=text: click(t)

    width = 13 if text == "0" else 6
    columnspan = 2 if text == "0" else 1

    tk.Button(
        root,
        text=text,
        font=("Arial",15),
        width=width,
        height=2,
        command=command
    ).grid(
        row=row,
        column=column,
        columnspan=columnspan,
        padx=3,
        pady=3
    )

tk.Button(
    root,
    text="=",
    font=("Arial",15),
    width=6,
    height=5,
    command=equal
).grid(
    row=6,
    column=4,
    rowspan=2,
    padx=3,
    pady=3
)

root.mainloop()