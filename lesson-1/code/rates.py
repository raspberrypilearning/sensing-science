#Investigating Rates of reaction
#Spencer Organ - KESH Academy

#Place the Sense Hat in a small plastic zip-lock sandwich bag

from sense_hat import SenseHat
sense = SenseHat()
import time
import sys


b = (0,0,255)
w = (255,255,255)
o = (0,0,0)

cross = [
b,w,w,w,w,w,w,b,
w,b,w,w,w,w,b,w,
w,w,b,w,w,b,w,w,
w,w,w,b,b,w,w,w,
w,w,b,w,w,b,w,w,
w,b,w,w,w,w,b,w,
b,w,w,w,w,w,w,b,
o,o,o,o,o,o,o,o
]


sense.clear(255,0,0)

concentration = float(input("Concentration of hydrochloric acid: "))
data = float(input("How many repeats do you want?: "))
file_name = input("File name for results ")
message1 = input("Press the button when you are ready to record the first result")

f = open(file_name, "w")

counter = 1

while counter <= data:
	temp = round(sense.get_temperature(),2)
	sense.set_pixels(cross)
	t1=time.time()
	press = input("Press the button when you can no longer see the cross")
	t2=time.time()
	print ("Experiment number ", counter)
	result = (round((t2-t1),2))
	counter +=1
	sense.clear(255,0,0)
	message = input("Press the button when you are ready to start the next result")
	f.write ("Investigating the change in temperature" + "\n")
	f.write (str(counter-2) + "|")
	f.write (str(concentration) + "|")
	f.write (str(temp) + "|")
	f.write (str(result) + "\n")
f.close()
sense.clear(0,0,0)