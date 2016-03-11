#Investigating fermentation of yeast
#Spencer Organ - KESH Academy

from picamera import PiCamera
from sense_hat import SenseHat
sense = SenseHat()
import time
import sys



def take_photo(number):
    time.sleep(300)
    with PiCamera() as camera:
        camera.start_preview()
        camera.capture('fermentation%s.jpg'%(number))
        timme.sleep(5)
        camera.stop_preview()
    sense.clear(black)

counter = 1

while counter <=12:
	take_photo(counter)
	counter +=1

