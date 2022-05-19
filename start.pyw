import tkinter
import tkinter as tk
import time
import sys
from subprocess import run
from tkinter import messagebox
from PIL import Image, ImageTk
try:
    import Tkinter as tk
except:
    import tkinter as tk

window = tkinter.Tk()
window.geometry("800x300")
window.title("Securepy")
window.attributes("-topmost", True)
window.overrideredirect(1)
window.update_idletasks()
w = window.winfo_width()
h = window.winfo_height()
scw = window.winfo_screenwidth()
sch = window.winfo_screenheight()
geometry = "+{:d}+{:d}".format(int((scw - w) / 2),
                               int((sch - h) / 2))
window.geometry(geometry)
img = Image.open('start.png')
img = ImageTk.PhotoImage(img)
canvas = tkinter.Canvas(bg = "black", width=800, height=300)
canvas.place(x=0, y=0)
canvas.create_image(0, 0, image=img, anchor=tkinter.NW)
def run_after():
    window.destroy()
    run(["python3","main.pyw"])
    return
window.after(6000, run_after)
window.mainloop()
