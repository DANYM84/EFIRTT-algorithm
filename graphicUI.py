from tkinter import *
from tkinter import ttk
from tkinter import filedialog
from PIL import Image, ImageDraw
from tkinter import messagebox
def browse_button():
    global folder_path
    filename = filedialog.askdirectory()
    folder_path.set(filename)
    return(filename)


root = Tk()
folder_path = StringVar()
lbl1 = Label(master=root,textvariable=folder_path)
lbl1.grid(row=2, column=2)
button2 = Button(text="Browse", command=browse_button)
button2.grid(row=2, column=2)

mainloop()