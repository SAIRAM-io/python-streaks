'''
Tkinter is the inbuilt GUI python module that is used to create GUI applications. It is one of the most commonly used modules for creating GUI applications in Python as it is simple and easy to work with.

Tk and Tkinter apps can run on most Unix platforms. This also works on Windows and Mac OS X.
'''

# Import tkinter
from tkinter import *

# Creating a window
window = Tk()

# Creating a Label Widget
label_1 = Label(window, text="Hello World!")
label_2 = Label(window, text="2nd line")

# Packing onto the window
label_1.pack()
label_2.pack()

label_3 = Label(window, text="3rd line....").pack()

# Running main loop
window.mainloop()

#############################################################################
# Grid packing

from tkinter import *
window = Tk()

label_1 = Label(window, text="Hello World!")
label_2 = Label(window, text="2nd line")

label_1.grid(row=0, column=0)
label_2.grid(row=1, column=1)

label_3 = Label(window, text="3rd line....").grid(row=1, column=2)

window.mainloop()

#############################################################################
# Buttons
from tkinter import *
window = Tk()

def sample(txt = None):
	if txt:
		my_label = Label(window, text=txt)
	else:
		my_label = Label(window, text="Button clicked!!")
	my_label.pack()

def even(num):
	if num%2 == 0:
		sample('Even number')
	else:
		sample('Odd number')

btn = Button(window, text="Click Me!!", command = sample)
btn.pack(pady=10, padx=10)
even_btn = Button(window, text="Is even??", command = lambda: even(5))
even_btn.pack(pady=10, padx=10)

window.mainloop()

#############################################################################
# To close the TKinter window programatically 

from tkinter import *

window = Tk()

quit_btn = Button(window, text="Exit program!!!", command=window.quit)
quit_btn.pack()

window.mainloop()

#############################################################################
# pack_forget() or destroy() --> to remove a widget from window
# add_text['state'] = DISABLED --> used to disable a button
# add_text['state'] = NORMAL --> used to enable a button
from tkinter import *
window = Tk()

def add():
	global my_label
	my_label = Label(window, text="Button clicked!!")
	my_label.pack(pady=10)
	add_text['state'] = DISABLED

def remove():
	# my_label.pack_forget()
	my_label.destroy()
	add_text['state'] = NORMAL

add_text = Button(window, text="Add label", command = add)
add_text.pack(pady=10, padx=10)

remove_text = Button(window, text="Remove Label", command = remove)
remove_text.pack(pady=10, padx=10)

window.mainloop()

#############################################################################
# Entry widget
from tkinter import *  
  
window = Tk()  
window.geometry("300x250") 

def submit():
	u_name = name_ew.get()
	u_email = email_ew.get()
	if not (len(u_name) < 1 or len(u_email) < 1):
		d_name = Label(window, text=f'Entered name: {u_name}')
		d_name.grid(row=4, column=0)
		d_email = Label(window, text=f'Entered email: {u_email}')
		d_email.grid(row=5, column=0)
	else:
		error_label = Label(window, text='Nothing entered!!!')
		error_label.grid(row=4, column=0)

def reset():
	name_ew.delete(0, 'end')
	email_ew.delete(0, 'end')
	password_ew.delete(0, 'end')

name = Label(window, text = "Name: ").grid(row=0, column=0, padx=10, pady=5)
email = Label(window, text = "Email: ").grid(row=1, column=0, padx=10, pady=5)
password = Label(window, text = "Password: ").grid(row=2, column=0, padx=10, pady=5)
submit_btn = Button(window, text = "Submit", command=submit).grid(row=3, column=0, padx=20, pady=5)
reset_btn = Button(window, text = "Reset", command=reset).grid(row=3, column=1, padx=20, pady=5)

name_ew = Entry(window)
name_ew.grid(row=0, column=1, padx=10, pady=5)
email_ew = Entry(window)
email_ew.grid(row=1, column=1, padx=10, pady=5)
password_ew = Entry(window, show='*')
password_ew.grid(row=2, column=1, padx=10, pady=5)
# print(help(name_ew))
window.mainloop()  

#############################################################################
# Working with Images
# import PIL module --> pip install pillow

from tkinter import *
from PIL import ImageTk, Image

window = Tk()
window.title('Image Gallery')
# window.iconbitmap("images/cat_1/pic_1.jpg")

img_1 = ImageTk.PhotoImage(Image.open("images/cat_1/pic_1.jpg"))
my_label = Label(image = img_1).grid(row=0, column=0, padx=20, pady=20)

img_2 = ImageTk.PhotoImage(Image.open("images/cat_1/pic_2.jpg"))
my_label = Label(image = img_2).grid(row=0, column=1, padx=20, pady=20)

window.mainloop()

#############################################################################
# Frames  
from tkinter import *

window = Tk()
window.title('Frames')

frame_1 = LabelFrame(window, padx=20, pady=20, text='Academic details')
frame_1.pack(padx=20, pady=10)

frame_2 = LabelFrame(window, padx=20, pady=20, text='Experience')
frame_2.pack(padx=20, pady=10)

frame_3 = LabelFrame(window, padx=20, pady=20, text='Projects')
frame_3.pack(padx=20, pady=10)

Button(frame_1, text="Frame 1 Button").pack(padx=20, pady=10)
Button(frame_1, text="Frame 1 Button").pack(padx=20, pady=10)

Button(frame_2, text="Frame 2 Button").pack(padx=20, pady=10)
Button(frame_2, text="Frame 2 Button").pack(padx=20, pady=10)

Button(frame_3, text="Frame 3 Button").pack(padx=20, pady=10)
Button(frame_3, text="Frame 3 Button").pack(padx=20, pady=10)


window.mainloop()

#############################################################################
# Radio buttons, Checkboxes and Message boxes
from tkinter import *
from tkinter import messagebox 

window = Tk()
window.title('Radio buttons')

def exit_func():
	val = messagebox.askquestion("askquestion", "Are you sure?")
	if val == 'yes':
		window.quit()

def submit():
	global h1, h2, h3
	global gender

	txt = 'Selected Hobbies --- '
	val = gender.get()
	if h1.get() != 'None':
		txt += '\n\t'+h1.get()
	if h2.get() != 'None':
		txt += '\n\t'+h2.get()
	if h3.get() != 'None':
		txt += '\n\t'+h3.get()
	print(txt)
	
	if val == 1:
		gender_txt = 'Male'
	elif val == 2:
		gender_txt = 'Female'
	elif val == 3:
		gender_txt = 'Others'
	else:
		messagebox.showerror("Submitted", "Please Choose your gender!!")
		return 
		# Label(window, text='Please Choose your gender').pack(anchor=CENTER, padx=20, pady=10)
	messagebox.showinfo("Submitted", f"Selected gender : {gender_txt}\n\n{txt}")
	# Label(window, text=f'Selected gender : {txt}').pack(anchor=CENTER, padx=20, pady=10)

gender = IntVar()
h1 = StringVar()
h2 = StringVar()
h3 = StringVar()

Radiobutton(window, text='Male', variable=gender, value=1).pack(padx=20, pady=5)
Radiobutton(window, text='Female', variable=gender, value=2).pack(padx=20, pady=5)
Radiobutton(window, text='Others', variable=gender, value=3).pack(padx=20, pady=5)

hc_1 = Checkbutton(window, text="Listening Music", variable=h1, onvalue="Listening Music", offvalue="None")
hc_1.pack(padx=20, pady=5)
hc_2 = Checkbutton(window, text="Browseing Internet", variable=h2, onvalue="Browseing Internet", offvalue="None")
hc_2.pack(padx=20, pady=5)
hc_3 = Checkbutton(window, text="Watching Movies", variable=h3, onvalue="Watching Movies", offvalue="None")
hc_3.pack(padx=20, pady=5)

hc_1.deselect()
hc_2.deselect()
hc_3.deselect()

submit_btn = Button(window, text="Submit", command=submit)
submit_btn.pack(anchor=CENTER, padx=20, pady=10)

exit_btn = Button(window, text="Exit", command=exit_func)
exit_btn.pack(anchor=E, padx=20, pady=10)

window.mainloop()

#############################################################################
# Creating new windows
from tkinter import *

window = Tk()
window.title('First window')
window.geometry('300x200')

def open_window():
	second_window = Toplevel()
	second_window.title('Second window')
	second_window.geometry('300x200')
	btn = Button(second_window, text="Close", command=second_window.destroy).pack(padx=20, pady=10)

Button(window, text="Open New Window", command=open_window).pack(padx=20, pady=10)
window.mainloop()

#############################################################################