import binascii
import nfc
import os
from pygame import mixer
import time
import tkinter
import tkinter as tk
from subprocess import run

class MyCardReader(object):
    def on_connect(self, tag):
        #タッチ時の処理
        #print("【 Touched 】")

        #タグ情報を全て表示
        print(tag)

        #IDmのみ取得して表示
        self.idm = binascii.hexlify(tag._nfcid)
        #print("IDm : " + str(self.idm))

        #特定のIDmだった場合のアクション
        if self.idm == b'011401148717a712':
            mixer.init()        #初期化
            mixer.music.load("beep.wav")
            mixer.music.play(1)
            #print("【 登録されたIDです 】")

        return True

    def read_id(self):
        clf = nfc.ContactlessFrontend('usb')
        try:
            clf.connect(rdwr={'on-connect': self.on_connect})
        finally:
            clf.close()

def card():
    if __name__ == '__main__':
        cr = MyCardReader()
        while True:
            #最初に表示
            #print("Please Touch")

            #タッチ待ち
            cr.read_id()

            #リリース時の処理
            #print("【 Released 】")

root = tkinter.Tk()
root.attributes('-topmost', True)
root.attributes('-fullscreen', True)
host = tk.PhotoImage(file="タッチ.png")
canvas = tk.Canvas(bg="black", width=1024, height=600)
canvas.place(x=0, y=0)
canvas.create_image(0, 0, image=host, anchor=tk.NW)
root.after(100, card)
root.mainloop()