import sys
import tkinter
from subprocess import run
from PIL import Image, ImageTk

time = 30
def count_down():
    global time
    time -= 1
    if time < 0:
        root.destroy()
        run(["python3","door.pyw"])
        sys.exit()
    label["text"]= time
    root.after(1000,count_down)

root = tkinter.Tk()
root.attributes('-topmost', True)
root.attributes('-fullscreen', True)
img = Image.open('警備開始猶予時間.png')
img = ImageTk.PhotoImage(img)
canvas = tkinter.Canvas(bg = "black", width=1024, height=600)
canvas.place(x=0, y=0)
canvas.create_image(0, 0, image=img, anchor=tkinter.NW)

label = tkinter.Label(font=("Arial", 100))
label.pack(anchor='center',expand=1)
root.after(1000,count_down)

root.mainloop()
