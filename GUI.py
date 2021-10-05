import tkinter as tk
from tkinter import ttk
from main import main
from main import get_god_image
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

root.mainloop()
