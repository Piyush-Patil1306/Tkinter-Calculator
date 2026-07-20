from tkinter import *

root = Tk()
root.title("Notepad")
root.geometry("480x650")
root.configure(bg="lightblue")

# 1. Defined BEFORE the widgets use it
def clear_text():
    txt.delete("1.0", END)
    txt.focus_set() # Puts the typing cursor back into the box automatically

label1 = Label(
    root,
    text="📝 Mini Notepad",
    bg="#2563EB",
    fg="white",
    font=("Segoe UI", 20, "bold"),
    pady=10
)
label1.pack(fill="x")

# 2. Packed at the bottom first
button_frame = Frame(root, bg="lightblue")
button_frame.pack(side=BOTTOM, fill=X, pady=15)

clearbtn = Button(
    button_frame,
    text="Clear",
    font=("Segoe UI", 12),
    width=15,
    command=clear_text # Pointing to the updated function name
)
clearbtn.pack()

# 3. Text widget packs last into the remaining space
txt = Text(
    root,
    font=("Segoe UI", 14)
)
txt.pack(
    fill=BOTH,
    expand=True,
    padx=10,
    pady=10
)

root.mainloop()