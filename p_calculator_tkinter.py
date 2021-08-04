from tkinter import *

window = Tk()
window.title("Mini Calculator")

e = Entry(window, width=45, borderwidth=3)
e.grid(row=0, column=0, columnspan=4, padx=10, pady=10)

exp = ''

def click_btn(num):
	current = e.get()
	e.delete(0, END)
	e.insert(0, current + num)

def button_clear():
	e.delete(0, END)

def add_btn():
	global exp
	exp += e.get()
	exp += '+'
	e.delete(0, END)

def subtract_btn():
	global exp
	exp += e.get()
	exp += '-'
	e.delete(0, END)

def multiply_btn():
	global exp
	exp += e.get()
	exp += '*'
	e.delete(0, END)

def divide_btn():
	global exp
	exp += e.get()
	exp += '/'
	e.delete(0, END)

def equal_btn():
	global exp, e
	exp += e.get()
	e.delete(0, END)
	e.insert(0, eval(exp))
	print('Result: ', exp, '=', eval(exp))
	exp = ''

btn_1 = Button(window, text="1", padx=40, pady=20, command=lambda: click_btn('1'))
btn_2 = Button(window, text="2", padx=40, pady=20, command=lambda: click_btn('2'))
btn_3 = Button(window, text="3", padx=40, pady=20, command=lambda: click_btn('3'))
btn_4 = Button(window, text="4", padx=40, pady=20, command=lambda: click_btn('4'))
btn_5 = Button(window, text="5", padx=40, pady=20, command=lambda: click_btn('5'))
btn_6 = Button(window, text="6", padx=40, pady=20, command=lambda: click_btn('6'))
btn_7 = Button(window, text="7", padx=40, pady=20, command=lambda: click_btn('7'))
btn_8 = Button(window, text="8", padx=40, pady=20, command=lambda: click_btn('8'))
btn_9 = Button(window, text="9", padx=40, pady=20, command=lambda: click_btn('9'))
btn_0 = Button(window, text="0", padx=40, pady=20, command=lambda: click_btn('0'))
btn_00 = Button(window, text="00", padx=40, pady=20, command=lambda: click_btn('00'))
btn_dot = Button(window, text=".", padx=40, pady=20, command=lambda: click_btn('.'))
btn_add = Button(window, text="+", padx=39, pady=20, command=add_btn)
btn_equal = Button(window, text="=", padx=91, pady=20, command=equal_btn)
btn_clear = Button(window, text="Clear", padx=79, pady=20, command=button_clear)

btn_subtract = Button(window, text="-", padx=41, pady=20, command=subtract_btn)
btn_multiply = Button(window, text="*", padx=40, pady=20, command=multiply_btn)
btn_divide = Button(window, text="/", padx=41, pady=20, command=divide_btn)

btn_7.grid(row=1, column=0)
btn_8.grid(row=1, column=1)
btn_9.grid(row=1, column=2)
btn_add.grid(row=1, column=3)

btn_4.grid(row=2, column=0)
btn_5.grid(row=2, column=1)
btn_6.grid(row=2, column=2)
btn_subtract.grid(row=2, column=3)

btn_1.grid(row=3, column=0)
btn_2.grid(row=3, column=1)
btn_3.grid(row=3, column=2)
btn_multiply.grid(row=3, column=3)

btn_0.grid(row=4, column=0)
btn_dot.grid(row=4, column=1)
btn_00.grid(row=4, column=2)
btn_divide.grid(row=4, column=3)

btn_clear.grid(row=5, column=0, columnspan=2)
btn_equal.grid(row=5, column=2, columnspan=2)

window.mainloop()
