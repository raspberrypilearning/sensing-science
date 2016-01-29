#Investigating stopping distances of cars
#Spencer Organ - KESH Academy


from sense_hat import SenseHat
sense = SenseHat()
import time
import sys
import random

sense.clear(255,255,255)

b = (0,0,0)
r = (255,0,0)
g = (0,255,0)
w = (255,255,255)

red_on = [
b,b,w,w,w,w,b,b,
b,b,w,r,r,w,b,b,
b,b,w,r,r,w,b,b,
b,b,w,w,w,w,b,b,
b,b,w,w,w,w,b,b,
b,b,w,b,b,w,b,b,
b,b,w,b,b,w,b,b,
b,b,w,w,w,w,b,b
]

green_on = [
b,b,w,w,w,w,b,b,
b,b,w,b,b,w,b,b,
b,b,w,b,b,w,b,b,
b,b,w,w,w,w,b,b,
b,b,w,w,w,w,b,b,
b,b,w,g,g,w,b,b,
b,b,w,g,g,w,b,b,
b,b,w,w,w,w,b,b
]

print ("Reaction time investigation" + '\n')
print ("This game will simulate the thinking distance component of stopping distance")
file_name = input("What is your class name ")
class_size = float(input("How many students in the class "))
speed = float(input("What is your speed in miles per hour "))

f = open(file_name, "w")

counter = 1

while counter <= class_size:

        student_name = input ("What is your name ")
        print ("Instruction", '\n', "As soon as you see the green traffic light turn red press the button on the Sense Hat")
        message1 = input("Press the button when you are ready to start")
        sense.set_pixels(green_on)
        wait = random.randint(3,10)
        time.sleep(wait)
        sense.clear(0,0,0)
        sense.set_pixels(red_on)
        start = time.time()
        message1 = input("Press the button")
        sense.clear(0,0,0)
        end = time.time()
        elapsed = end - start
        print ("You took " + str(round(elapsed,2)) + " seconds to press the button")
        distance = round(((speed * 0.44704)*elapsed),2)
        print ("At " + str(speed) + " miles per hour you would have travelled " + str(distance) + " m")

## Write the data to the file and repeat for the next student in the class

        f.write (str(counter) + "|")
        f.write (str(speed) + "|")
        f.write (student_name + "|")
        f.write (str(round(elapsed,2)) + "|")
        f.write (str(distance) + "\n")
        counter +=1

f.close()
sense.clear(0,0,0)
        


