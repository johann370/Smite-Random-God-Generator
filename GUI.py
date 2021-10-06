import tkinter as tk
from tkinter import ttk
from main import *
from PIL import Image, ImageTk

root = tk.Tk()
root.title('Random God Generator')
root.geometry('1000x1000')
image_label = ttk.Label(root)
name_label = ttk.Label(root, font=('Helvetica', 20))


def button_clicked():
    random_god = main()
    god_image_path = get_god_image(random_god)
    god_image = ImageTk.PhotoImage(Image.open(god_image_path))
    image_label.configure(image=god_image)
    image_label.image = god_image
    name_label.configure(text=random_god.get_name())
    name_label.pack()
    image_label.pack()
    button.configure(text='Reroll')


button = ttk.Button(root, text='Get God', command=button_clicked)
button.pack()

checkbuttonVariables = dict()


def create_filter_gods_window():
    filter_window = tk.Toplevel(root)
    content = ttk.Frame(filter_window)
    gods = get_gods_list()
    grid_row = 0
    grid_col = 0
    content.pack()

    for god in gods:
        checkbuttonVariables[f'{god.get_name()}'] = tk.BooleanVar(value=True)
        cb = ttk.Checkbutton(content, text=f'{god.get_name()}', padding=15,
                             variable=checkbuttonVariables[f'{god.get_name()}'],
                             onvalue=True, offvalue=False)
        cb.grid(column=grid_col, row=grid_row)
        if (grid_col == 5):
            grid_col = 0
            grid_row += 1
        else:
            grid_col += 1


filter_button = ttk.Button(root, text='Filter Gods', command=create_filter_gods_window)
filter_button.pack()

root.mainloop()
