#Investigating Choice chambers
#Spencer Organ - KESH Academy

from picamera import PiCamera
from sense_hat import SenseHat
sense = SenseHat()
import time
import sys

sense.clear(0,0,0)

black = (0,0,0)
red = (255,0,0)
green = (0,255,0)
blue = (0,0,255)
white = (255,255,255)

def illuminate_matrix(a,b,c,d):
    matrix = [
    a,a,a,a,b,b,b,b,
    a,a,a,a,b,b,b,b,
    a,a,a,a,b,b,b,b,
    a,a,a,a,b,b,b,b,
    c,c,c,c,d,d,d,d,
    c,c,c,c,d,d,d,d,
    c,c,c,c,d,d,d,d,
    c,c,c,c,d,d,d,d
    ]
    sense.set_pixels(matrix)

def take_photo(number):
    time.sleep(30)
    with PiCamera() as camera:
        camera.start_preview()
        camera.capture('choice%s.jpg'%(number))
        timme.sleep(5)
        camera.capture('second_choice%s.jpg'%(number))
        camera.stop_preview()
    sense.clear(black)

print ("Place the insects ontop of the LED maxtrix in a petri dish")
print ("This will cycle through the standard colours taking a photo after 20 seconds")


counter = 1

## Edit the colours to change the sequence of photos

## All white
illuminate_matrix(white,white,white,white)
take_photo(counter)
counter +=1

## half white
illuminate_matrix(white,white,black,black)
take_photo(counter)
counter +=1

## quarter white
illuminate_matrix(white,black,black,black)
take_photo(counter)
counter +=1

## All red
illuminate_matrix(red,red,red,red)
take_photo(counter)
counter +=1

## half red
illuminate_matrix(red,red,black,black)
take_photo(counter)
counter +=1

## quarter red
illuminate_matrix(red,black,black,black)
take_photo(counter)
counter +=1

## All blue
illuminate_matrix(blue,blue,blue,blue)
take_photo(counter)
counter +=1

## half blue
illuminate_matrix(blue,blue,black,black)
take_photo(counter)
counter +=1

## quarter blue
illuminate_matrix(blue,black,black,black)
take_photo(counter)
counter +=1

## All green
illuminate_matrix(green,green,green,green)
take_photo(counter)
counter +=1

## half green
illuminate_matrix(green,green,black,black)
take_photo(counter)
counter +=1

## quarter green
illuminate_matrix(green,black,black,black)
take_photo(counter)
counter +=1

## green and blue
illuminate_matrix(green,green,blue,blue)
take_photo(counter)
counter +=1

## green and red
illuminate_matrix(green,green,red,red)
take_photo(counter)
counter +=1

## red and blue
illuminate_matrix(red,red,blue,blue)
take_photo(counter)
counter +=1
