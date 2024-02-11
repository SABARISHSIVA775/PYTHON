from tkinter import *

expression = ""

def press(num):
    global expression
    expression = expression + str(num)
    equation.set(expression)

def equalpress():
    try:
        global expression
        total = str(eval(expression))
        equation.set(total)
        expression = ""
    except:
        equation.set("Error")
        expression = ""

def clear():
    global expression
    expression = ""
    equation.set("")

gui = Tk()
gui.title("Simple Calculator")
gui.configure(background="black")
gui.geometry("350x450")

equation = StringVar()

expression_field = Entry(gui, textvariable=equation, font=('Arial', 20), bd=10, insertwidth=1, width=20, justify='right')
expression_field.grid(row=0, column=0, columnspan=4, pady=10)

button_style = {'font': ('TimesNewRoman', 15), 'bd': 5, 'bg': 'skyblue', 'fg': 'black', 'width': 5, 'height': 2}

buttons = [
    ('7', 1, 0), ('8', 1, 1), ('9', 1, 2), ('/', 1, 3),
    ('4', 2, 0), ('5', 2, 1), ('6', 2, 2), ('*', 2, 3),
    ('1', 3, 0), ('2', 3, 1), ('3', 3, 2), ('-', 3, 3),
    ('0', 4, 0), ('C', 4, 1), ('=', 4, 2), ('+', 4, 3)
]

for (text, row, col) in buttons:
    if text == 'C':
        btn = Button(gui, text=text, **button_style, command=clear)
    elif text == '=':
        btn = Button(gui, text=text, **button_style, command=equalpress)
    else:
        btn = Button(gui, text=text, **button_style, command=lambda t=text: press(t))
    btn.grid(row=row, column=col, padx=5, pady=5)

gui.mainloop()
