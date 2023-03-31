import qrcode
from tkinter import messagebox, Tk, Label, Entry, Button
from tkinter import filedialog
from PIL import Image, ImageDraw
from main import captureIMG


def browse_button():
    global folder_path
    filename = filedialog.askdirectory()
    captureIMG(filename)



if __name__ == '__main__':
    window = Tk()
    window.title("EFIRTT-algorithm")
    window.config(padx=10, pady=100)

    # Labels
    website_label = Label(text="Caminho da Pasta:")
    website_label.grid(row=4, column=0)

    # Entries
    
    
    add_button = Button(text="Procurar Pasta", width=36, command=browse_button)
    add_button.grid(row=4, column=1, columnspan=2)
    window.mainloop()