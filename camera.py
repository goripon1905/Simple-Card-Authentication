from picamera import PiCamera
from time import sleep
import RPi.GPIO as GPIO
import time
import datetime

camera = PiCamera()

GPIO.setmode(GPIO.BCM)
GPIO.setup(18,GPIO.IN,pull_up_down=GPIO.PUD_UP)

x = 0
y = 1
doorsensor = 1

while True:
    try:
        doorsensor = GPIO.input(18)
        if doorsensor == 0:
            print("クローズ")
            datetime.datetime.now()
        else:
            print("オープン")
            now = datetime.datetime.now()
            while True:
                i = x
                cnt = y
                if i is not cnt:
                    i = i + 1
                    cnt = cnt + 1
                    X = i
                    y = cnt
                    camera.start_recording('/home/pi/動画/now%s.h264' % i)
                    sleep(5)
                    camera.stop_recording()
                break
            time.sleep(0.03)
    except:
        break

GPIO.cleanup()
print("end")


#camera.start_preview()

#camera.stop_preview()
