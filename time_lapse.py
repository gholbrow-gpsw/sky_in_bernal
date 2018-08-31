from picamera import PiCamera
from time import sleep
from datetime import datetime, time
from scipy import ndimage, misc
import matplotlib.pyplot as plt

#returns True if time laps is valid (5 am through 10pm)

def is_time_lapse_time():
    now = datetime.now()
    now_time = now.time()
    if now_time >= time(5,00) and now_time <= time(22,00):
        return True
    else:
        return False
    
def run_lapse():
    camera = PiCamera()
    camera.iso = 100
    camera.awb_mode = 'sunlight'
    camera.shutter_speed = 500
                      
    i = 0
    while is_time_lapse_time() == True:        
        camera.capture('/home/pi/CODE/sky_in_bernal/test_images/image%s.jpg' % i) 
        i += 1
        sleep(300)

run_lapse()        
#face = misc.imread('/home/pi/CODE/sky_in_bernal/test_images/test.jpg')
#face_slice = face[10:13, 20:23, :]


#plt.imshow(face)

#camera.capture('/home/pi/CODE/sky_in_bernal/test_images/test.jpg')






