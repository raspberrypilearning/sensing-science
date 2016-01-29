#Cooling curves investigation
#Spencer Organ - KESH Academy

from sense_hat import SenseHat
sense = SenseHat()
import time
import sys

file_name = input("file name for results ")
material = input ("Black or Silver? ")
interval = float(input ("How much time do you want between each measurement "))
measurements = float(input("How many measurements do you want to take "))
time_delay = float(input("Time before measurements start, I suggest 5 minutes"))

f = open(file_name, "w")

counter = 0

print ("Waiting for Raspberry Pi to warm up")

time.sleep(time_delay)

print ("Remove the heat source from the Raspberry Pi and Sense Hat")

while counter <= measurements:

    temp = round(sense.get_temperature(),2)
    f.write (material + "|")
    f.write (str(counter) + "|")
    f.write (str(temp) + "\n")
    counter +=1
    time.sleep(interval)
    print (temp)
f.close()

print ("All results recorded")
