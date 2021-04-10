from tkinter import *
from PIL import ImageTk, Image

window = Tk()
window.title('Image Viewer')

def forward(img_num):
	clear_screen(1)
	global my_label, btn_forward, btn_back, btn_categories

	my_label.destroy()
	my_label = Label(image = images[img_num-1])

	btn_categories = Button(window, text = "Go to Categories", command = clear_screen)
	btn_categories.grid(row = 0, column = 0, padx=20, pady=10)
	btn_forward = Button(window, text = "next", command = lambda: forward(img_num+1))
	btn_back = Button(window, text = "back", command = lambda: back(img_num-1))
	
	if img_num == len(images):
		btn_forward = Button(window, text = "next", state = DISABLED)

	my_label.grid(row = 1, column = 0, columnspan = 3)
	btn_back.grid(row = 2, column = 0, padx=20, pady=10)
	btn_forward.grid(row = 2, column = 2, padx=20, pady=10)
	# clear_screen()

def back(img_num):
	clear_screen(1)
	global my_label, btn_forward, btn_back, btn_categories
	my_label.destroy()
	my_label = Label(image = images[img_num-1])

	btn_categories = Button(window, text = "Go to Categories", command = clear_screen)
	btn_categories.grid(row = 0, column = 0, padx=20, pady=10)

	btn_forward = Button(window, text = "next", command = lambda: forward(img_num+1))
	btn_back = Button(window, text = "back", command = lambda: back(img_num-1))

	if img_num == 1:
		btn_back = Button(window, text = "back", state = DISABLED)

	my_label.grid(row = 1, column = 0, columnspan = 3)
	btn_back.grid(row = 2, column = 0, padx=20, pady=10)
	btn_forward.grid(row = 2, column = 2, padx=20, pady=10)
	# clear_screen()

def initial_setup(cat_name):
	global cat_1, cat_2, cat_3
	global images, my_label, btn_back, btn_forward, btn_categories

	cat_1.destroy()
	cat_2.destroy()
	cat_3.destroy()

	no_of_images = 6
	for i in range(no_of_images):
		filename = "images/{}/pic_{}.jpg".format(cat_name,i+1)
		img = ImageTk.PhotoImage(Image.open(filename))
		images.append(img)

	btn_categories = Button(window, text = "Go to Categories", command = clear_screen)
	btn_categories.grid(row = 0, column = 0, padx=20, pady=10)

	my_label = Label(image = images[0])
	my_label.grid(row = 1, column = 0, columnspan = 3)

	btn_back = Button(window, text = "back", command = back, state = DISABLED)
	btn_forward = Button(window, text = "next", command = lambda: forward(2))

	btn_back.grid(row = 2, column = 0, padx=20, pady=10)
	btn_forward.grid(row = 2, column = 2, padx=20, pady=10)

def clear_screen(flag = 0):
	global images, my_label, btn_back, btn_forward, btn_categories
	my_label.destroy()
	btn_back.destroy()
	btn_forward.destroy()
	btn_categories.destroy()
	if flag == 0: 
		images = []
		categories()

def categories():
	global cat_1, cat_2, cat_3
	cat_1 = Button(window, text='Marvel', padx=5, pady=5, command = lambda: initial_setup('cat_1'))
	cat_1.grid(row = 0, column = 0, padx=20, pady=10)
	cat_2 = Button(window, text='Tom & Jerry', padx=5, pady=5, command = lambda: initial_setup('cat_2'))
	cat_2.grid(row = 0, column = 1, padx=20, pady=10)
	cat_3 = Button(window, text='Joker', padx=5, pady=5, command = lambda: initial_setup('cat_3'))
	cat_3.grid(row = 1, column = 0, padx=20, pady=10)

images = []
categories()
window.mainloop()