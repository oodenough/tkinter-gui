from tkinter import *
from PIL import ImageTk, Image

root = Tk()
root.title('icon and image')
root.iconbitmap('/imgs/icon.ico')
# icon = PhotoImage(file='./imgs/icon.png')
# root.iconphoto(True, icon)

my_img = ImageTk.PhotoImage(Image.open('./imgs/image.png'))
my_label = Label(image=my_img)
my_label.pack()
button_exit = Button(root, text='Exit', command=root.quit)
button_exit.pack()


root.mainloop()