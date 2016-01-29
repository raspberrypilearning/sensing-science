#Investigating Respiration using the Sense Hat
#Spencer Organ - KESH Academy

#Place the Sense Hat in a plastic zip-lock sandwich bag with a drinking straw sticking out

from sense_hat import SenseHat
sense = SenseHat()
import time

B = (0,0,0)
b = (0,0,255)
w = (255,255,255)

cell = [
B,B,B,b,b,B,B,B,
B,B,b,b,b,B,B,B,
B,b,b,b,b,b,B,B,
B,b,b,w,w,b,b,B,
B,b,b,w,w,b,b,B,
B,b,b,b,b,b,b,B,
B,B,b,b,b,b,b,B,
B,B,B,b,b,b,B,B
]


sense.clear()
sense.set_pixels(cell)

#Wait until the enter button is pressed on the Sense Hat

wait = input("Press<enter> to continue")

sense.clear(0,0,255)
#Blow now
time.sleep(10)
sense.clear(255,0,0)

#Collect data for the first experiment

humidity_start = round(sense.get_humidity(),2)
temp_start = round(sense.get_temperature(),2)

#Start exercise
sense.clear(255,255,0)
time.sleep(15)

sense.clear(0,0,255)
#Blow now
time.sleep(10)
sense.clear(255,0,0)

humidity_end = round(sense.get_humidity(),2)
temp_end = round(sense.get_temperature(),2)

print("Humidity at the start of the test: %s %%rH" % humidity_start)
print("Temperature: %s C" % temp_start)
print("Humidity at the end of the test: %s %%rH" % humidity_end)
print("Temperature: %s C" % temp_end)

sense.clear()