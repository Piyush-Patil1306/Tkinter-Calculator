import tkinter as tk

root = tk.Tk()
root.title("Scientific Calculator")
root.geometry("470x650")
root.resizable(False, False)

display = tk.Entry(
    root,
    font=("Arial", 30),
    justify="right",
    width=20,
    bd=5
)

display.grid(
    row=0,
    column=0,
    columnspan=5,
    padx=10,
    pady=(20,10),
    ipady=15
)

message = tk.Label(
    root,
    text="",
    fg="red",
    font=("Arial",12)
)

message.grid(row=1,column=0,columnspan=5)

def one():
    display.insert(tk.END,"1")

def two():
    display.insert(tk.END,"2")

def three():
    display.insert(tk.END,"3")

def four():
    display.insert(tk.END,"4")

def five():
    display.insert(tk.END,"5")

def six():
    display.insert(tk.END,"6")

def seven():
    display.insert(tk.END,"7")

def eight():
    display.insert(tk.END,"8")

def nine():
    display.insert(tk.END,"9")

def zero():
    display.insert(tk.END,"0")

def plus():
    display.insert(tk.END,"+")

def minus():
    display.insert(tk.END,"-")

def multiply():
    display.insert(tk.END,"*")

def divide():
    display.insert(tk.END,"/")

def decimal():
    display.insert(tk.END,".")

def open_bracket():
    display.insert(tk.END,"(")

def close_bracket():
    display.insert(tk.END,")")

def square():
    display.insert(tk.END,"²")

def square_root():
    display.insert(tk.END,"√")

def logarithm():
    display.insert(tk.END,"log(")

def natural_log():
    display.insert(tk.END,"ln(")

def percent():
    display.insert(tk.END,"%")

def clear():
    display.delete(0,tk.END)
    message.config(text="")

def equal():
    message.config(text="Function Coming Soon")

tk.Button(root,text="(",font=("Arial",15),width=6,height=2,command=open_bracket).grid(row=2,column=0,padx=3,pady=3)

tk.Button(root,text=")",font=("Arial",15),width=6,height=2,command=close_bracket).grid(row=2,column=1,padx=3,pady=3)

tk.Button(root,text="√",font=("Arial",15),width=6,height=2,command=square_root).grid(row=2,column=2,padx=3,pady=3)

tk.Button(root,text="x²",font=("Arial",15),width=6,height=2,command=square).grid(row=2,column=3,padx=3,pady=3)

tk.Button(root,text="C",font=("Arial",15),width=6,height=2,command=clear).grid(row=2,column=4,padx=3,pady=3)

tk.Button(root,text="log",font=("Arial",15),width=6,height=2,command=logarithm).grid(row=3,column=0,padx=3,pady=3)

tk.Button(root,text="ln",font=("Arial",15),width=6,height=2,command=natural_log).grid(row=3,column=1,padx=3,pady=3)

tk.Button(root,text="%",font=("Arial",15),width=6,height=2,command=percent).grid(row=3,column=2,padx=3,pady=3)

tk.Button(root,text="/",font=("Arial",15),width=6,height=2,command=divide).grid(row=3,column=3,padx=3,pady=3)

tk.Button(root,text="*",font=("Arial",15),width=6,height=2,command=multiply).grid(row=3,column=4,padx=3,pady=3)

tk.Button(root,text="7",font=("Arial",15),width=6,height=2,command=seven).grid(row=4,column=0,padx=3,pady=3)

tk.Button(root,text="8",font=("Arial",15),width=6,height=2,command=eight).grid(row=4,column=1,padx=3,pady=3)

tk.Button(root,text="9",font=("Arial",15),width=6,height=2,command=nine).grid(row=4,column=2,padx=3,pady=3)

tk.Button(root,text="-",font=("Arial",15),width=6,height=2,command=minus).grid(row=4,column=3,padx=3,pady=3)

tk.Button(root,text="4",font=("Arial",15),width=6,height=2,command=four).grid(row=5,column=0,padx=3,pady=3)

tk.Button(root,text="5",font=("Arial",15),width=6,height=2,command=five).grid(row=5,column=1,padx=3,pady=3)

tk.Button(root,text="6",font=("Arial",15),width=6,height=2,command=six).grid(row=5,column=2,padx=3,pady=3)

tk.Button(root,text="+",font=("Arial",15),width=6,height=2,command=plus).grid(row=5,column=3,padx=3,pady=3)

tk.Button(root,text="1",font=("Arial",15),width=6,height=2,command=one).grid(row=6,column=0,padx=3,pady=3)

tk.Button(root,text="2",font=("Arial",15),width=6,height=2,command=two).grid(row=6,column=1,padx=3,pady=3)

tk.Button(root,text="3",font=("Arial",15),width=6,height=2,command=three).grid(row=6,column=2,padx=3,pady=3)

tk.Button(root,text="=",font=("Arial",15),width=6,height=5,command=equal).grid(row=6,column=4,rowspan=2,padx=3,pady=3)

tk.Button(root,text="0",font=("Arial",15),width=13,height=2,command=zero).grid(row=7,column=0,columnspan=2,padx=3,pady=3)

tk.Button(root,text=".",font=("Arial",15),width=6,height=2,command=decimal).grid(row=7,column=2,padx=3,pady=3)

tk.Button(root,text="+/-",font=("Arial",15),width=6,height=2).grid(row=7,column=3,padx=3,pady=3)

root.mainloop()