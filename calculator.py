from tkinter import *

root = Tk()
root.title("计算器")

e = Entry(root, width=35, borderwidth=5)
e.grid(row=0, column=0, columnspan=3, padx=10, pady=10)

def button_click(number):
    # result = str(e.get()) + str(number)
    # e.delete(0, END)
    # e.insert(0, int(result))
    e.insert(END, number)

def button_clear():
    e.delete(0, END)

def button_equal():
    operand2 = int(e.get())
    e.delete(0, END)
    global operand1, operator
    if operator == '+':
        e.insert(0, operand1 + operand2)
    elif operator == '-':
        e.insert(0, operand1 - operand2)
    elif operator == '*':
        e.insert(0, operand1 * operand2)
    elif operator == '/':
        e.insert(0, operand1 / operand2)
    else:
        e.insert('Error!')

def button_cal(symbol):
    global operand1, operator
    operator = symbol
    operand1 = int(e.get())
    e.delete(0, END)

# define buttons
button_1 = Button(root, text="1", padx=40, pady=20, command=lambda: button_click(1))
button_2 = Button(root, text="2", padx=40, pady=20, command=lambda: button_click(2))
button_3 = Button(root, text="3", padx=40, pady=20, command=lambda: button_click(3))
button_4 = Button(root, text="4", padx=40, pady=20, command=lambda: button_click(4))
button_5 = Button(root, text="5", padx=40, pady=20, command=lambda: button_click(5))
button_6 = Button(root, text="6", padx=40, pady=20, command=lambda: button_click(6))
button_7 = Button(root, text="7", padx=40, pady=20, command=lambda: button_click(7))
button_8 = Button(root, text="8", padx=40, pady=20, command=lambda: button_click(8))
button_9 = Button(root, text="9", padx=40, pady=20, command=lambda: button_click(9))
button_0 = Button(root, text="0", padx=40, pady=20, command=lambda: button_click(0))

button_add = Button(root, text="+", padx=40, pady=20, fg="blue", command=lambda: button_cal('+'))
button_sub = Button(root, text="-", padx=40, pady=20, fg="blue", command=lambda: button_cal('-'))
button_mul = Button(root, text="x", padx=40, pady=20, fg="blue", command=lambda: button_cal('*'))
button_div = Button(root, text="÷", padx=40, pady=20, fg="blue", command=lambda: button_cal('/'))

button_equal = Button(root, text="=", padx=40, pady=55, fg="red", command=button_equal)
button_clear = Button(root, text="Clear", padx=90, pady=20, fg="red", command=button_clear)

button_1.grid(row=3, column=0)
button_2.grid(row=3, column=1)
button_3.grid(row=3, column=2)
button_4.grid(row=2, column=0)
button_5.grid(row=2, column=1)
button_6.grid(row=2, column=2)
button_7.grid(row=1, column=0)
button_8.grid(row=1, column=1)
button_9.grid(row=1, column=2)
button_0.grid(row=4, column=0)

button_clear.grid(row=4, column=1, columnspan=2)
button_equal.grid(row=5, column=2, rowspan=2)

button_add.grid(row=5, column=0)
button_sub.grid(row=5, column=1)
button_mul.grid(row=6, column=0)
button_div.grid(row=6, column=1)

root.mainloop()