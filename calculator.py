from tkinter import *


def click(event):
    global expr
    text = event.widget.cget("text")

    if text == "=":
        try:
            result = str(eval(expr))
            entry_var.set(result)
            expr = result
        except:
            entry_var.set("Error")
            expr = ""
    elif text == "C":
        expr = ""
        entry_var.set("")
    else:
        expr += text
        entry_var.set(expr)


def key(event):
    global expr
    key = event.char
    if key in "0123456789+-*/.":
        expr += key
        entry_var.set(expr)
    elif key == "\r":
        try:
            result = str(eval(expr))
            entry_var.set(result)
            expr = result
        except:
            entry_var.set("Error")
            expr = ""
    elif event.keysym == "BackSpace":
        expr = expr[:-1]
        entry_var.set(expr)
    elif key.lower() == "c":
        expr = ""
        entry_var.set("")


root = Tk()
root.title("Calculator")
root.geometry("270x350")

expr = ""
entry_var = StringVar()

entry = Entry(root, textvar=entry_var, font="Arial 20", justify=RIGHT, bd=8)
entry.pack(fill=BOTH, ipadx=8, pady=10, padx=10)
entry.focus()

root.bind("<Key>", key)

btns = [
    ['7', '8', '9', '/'],
    ['4', '5', '6', '*'],
    ['1', '2', '3', '-'],
    ['0', '.', 'C', '+'],
    ['=']
]

for row in btns:
    f = Frame(root)
    f.pack(expand=True, fill=BOTH)
    for b in row:
        btn = Button(f, text=b, font="Arial 16")
        btn.pack(side=LEFT, expand=True, fill=BOTH)
        btn.bind("<Button-1>", click)

root.mainloop()
