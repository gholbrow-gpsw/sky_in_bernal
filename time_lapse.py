from picamera import PiCamera
from time import sleep
from datetime import datetime, time
#returns True if time laps is valid (5 am through 10pm)


now = datetime.now()
now_time = now.time()
if now_time >= time(5,00) and now_time <= time(22,00):
    print("yes, within the interval")

    
camera = PiCamera()

#camera.capture('/home/pi/CODE/sky_in_bernal/test_images/test.jpg')






