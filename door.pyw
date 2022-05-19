import time
import tkinter
import tkinter as tk
import RPi.GPIO as GPIO
from subprocess import run

GPIO.setmode(GPIO.BCM)
GPIO.setup(18, GPIO.IN, pull_up_down=GPIO.PUD_UP)
sw_status = 1

def stop():
    GPIO.cleanup()
    root.destroy()
    run(["python3","main.pyw"])

def door():
    try:
        sw_status = GPIO.input(18)
        if sw_status == 0:
            root.after(100, door)
        else:
            root.after(100, stop)
        time.sleep(2)
    except:
        root.after(100, stop)


root = tkinter.Tk()
root.attributes('-topmost', True)
root.attributes('-fullscreen', True)
host = tk.PhotoImage(file="警備中.png")
canvas = tk.Canvas(bg="black", width=1024, height=600)
canvas.place(x=0, y=0)
canvas.create_image(0, 0, image=host, anchor=tk.NW)
root.after(100, door)
root.mainloop()
