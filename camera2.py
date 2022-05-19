from picamera import PiCamera
from time import sleep
import RPi.GPIO as GPIO
import time
import datetime

camera = PiCamera()

GPIO.setmode(GPIO.BCM)
GPIO.setup(18,GPIO.IN,pull_up_down=GPIO.PUD_UP)

cnt = 0
doorsensor = 1

datetime.datetime.now()
now = datetime.datetime.now()
save_dir = "./output/log_"
filename = "./output/log_" + now.strftime('%Y%m%d_%H%M%S') + '.csv'
f = open(filename, 'w')
writer = csv.writer(f, lineterminator='\n') 

while True:
    try:
        doorsensor = GPIO.input(18)
        if doorsensor == 0:
            print("クローズ")
        else:
            print("オープン")
            datetime.datetime.now()
            now = datetime.datetime.now()
            filename = './output/log_' + now.strftime('%Y%m%d_%H%M%S') + '.csv'
            f = open(filename, 'w')
            writer = csv.writer(f, lineterminator='\n')
            
            a = [1,2,3]
            writer.writerow(a)

            b = np.array([10, 20, 30])
            writer.writerow(b.tolist())

            writer.writerow(["日付",now])
            writer.writerow(["日付",now.strftime('%Y/%m/%d'),now.strftime('%H:%M:%S')])

            camera.start_recording(save_dir + now + ".h264")
            sleep(15)
            camera.stop_recording()

        time.sleep(0.03)
    except:
        break

GPIO.cleanup()
print("end")
