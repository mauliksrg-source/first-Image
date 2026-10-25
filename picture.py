import tkinter as tk
from PIL import Image, ImageTk
root=tk.Tk()
root.geometry("600x600")
root.title("Image")
root.configure(bg="orange")
a=Image.open("C:/Users/MSG/OneDrive/Python/picturepython.jpg")
tkImage=ImageTk.PhotoImage(a)
l=tk.Label(root, image=tkImage)
l.place(relx=0.5, rely=0.5, anchor="center")
root.mainloop()