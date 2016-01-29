#Investigating Black and Silver cans
#Spencer Organ - KESH Academy

#Wrap the Sense Hat in either black paper or silver foil.  Ensure that you know which way is up!

from sense_hat import SenseHat
sense = SenseHat()
import time
import sys

file_name = input("File name for results ")
material = input("Black or Silver? ")
measurements = float(input("How many measurements do you want to record: "))
interval = float(input("How long do you want to wait between each measurement: "))
message1 = input("Press the button or the enter key when you are ready to start recording")

f = open(file_name, "w")

counter = 0

while counter <= measurements:
	temp = round(sense.get_temperature(),2)
	f.write (material + "|")
	f.write (str(counter) + "|")
	f.write (str(temp) + "\n")
	counter +=1
	time.sleep(interval)
f.close()
