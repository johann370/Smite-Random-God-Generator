import tkinter as tk
from tkinter import ttk
from get_random_god import *
from PIL import Image, ImageTk


def initialize_checkbutton_variables(gods, checkbutton_variables):
    for god in gods:
        checkbutton_variables[f'{god.get_name()}'] = tk.BooleanVar(value=True)


def button_clicked(gods, image_label, name_label, button, checkbutton_variables):
    filtered_gods = get_filtered_gods(gods, checkbutton_variables)
    if len(filtered_gods) > 0:
        random_god = get_random_god(filtered_gods)

        god_image_path = get_god_image(random_god)
        god_image = ImageTk.PhotoImage(Image.open(god_image_path))
        image_label.configure(image=god_image)
        image_label.image = god_image

        name_label.configure(text=random_god.get_name())

        name_label.pack()
        image_label.pack()
        button.configure(text='Reroll')


def get_filtered_gods(gods, checkbutton_variables):
    filtered_gods = list()
    for god in gods:
        if checkbutton_variables[f'{god.get_name()}'].get():
            filtered_gods.append(god)
    return filtered_gods


def create_filter_gods_window(root, checkbutton_variables):
    filter_window = tk.Toplevel(root)
    content = ttk.Frame(filter_window)
    gods = get_gods_list()
    grid_row = 0
    grid_col = 0
    content.pack()

    for god in gods:
        cb = ttk.Checkbutton(content, text=f'{god.get_name()}', padding=15,
                             variable=checkbutton_variables[f'{god.get_name()}'],
                             onvalue=True, offvalue=False)
        cb.grid(column=grid_col, row=grid_row)
        if grid_col == 5:
            grid_col = 0
            grid_row += 1
        else:
            grid_col += 1


def main():
    root = tk.Tk()
    root.title('Random God Generator')
    root.geometry('1000x1000')
    image_label = ttk.Label(root)
    name_label = ttk.Label(root, font=('Helvetica', 20))

    checkbutton_variables = dict()
    gods = get_gods_list()

    initialize_checkbutton_variables(gods, checkbutton_variables)

    button = ttk.Button(root, text='Get God', command=lambda : button_clicked(gods, image_label, name_label, button, checkbutton_variables))
    button.pack()

    filter_button = ttk.Button(root, text='Filter Gods', command=lambda: create_filter_gods_window(root, checkbutton_variables))
    filter_button.pack()

    root.mainloop()