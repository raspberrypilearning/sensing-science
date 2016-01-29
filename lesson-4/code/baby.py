#Keeping Baby warm - an investigation in insulation
#Spencer Organ - KESH Academy

from sense_hat import SenseHat
sense = SenseHat()
import time
import sys

file_name = input("file name for results ")
material = input ("Material used to keep the baby warm ")
interval = float(input ("How much time do you want between each measurement "))
measurements = float(input("How many measurements do you want to take "))

f = open(file_name, "w")

counter = 0

print ("Waiting for the Baby to warm up. This will take 5 minutes")

#time.sleep(270)

print ("Get ready to remove the baby (the heat source) from the Raspberry Pi")
#time.sleep(30)

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
