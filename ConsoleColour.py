import random
from sty import fg

#WORKS ON LINUX

def generateRGB():
    red = random.randint(0,256)
    green = random.randint(0,256)
    blue = random.randint(0,256)
    return red, green, blue

def generateColour(red, green, blue):
    return fg(red, green, blue)

red, green, blue = generateRGB()
colour = generateColour(red, green, blue)

print(colour, "I'm randomly changing colours muahahahahahaha!!", fg.rs)