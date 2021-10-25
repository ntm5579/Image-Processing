from tkinter import *
from random import randint
from PIL import Image, ImageColor

#auto mode bypasses input, for testing
'''
auto = input("Yes or No: ")
if auto.lower() == "yes":
    size = 500
    rgb = False
else:'''
#must indent line 13 and 14 when automode is uncommented
size = int(input("How big of a noise square do you want? "))
rgb = bool(input("Do you want rgb? True or False "))

#determines what mode the image is created in
if rgb:
    #rgb mode
    im = Image.new('RGB', (size,size))
else:
    #grayscale mode
    im = Image.new('L', (size,size)) # create the Image of size 1 pixel

for i in range(size):
    for j in range(size):
        if rgb:
            #rgb mode
            im.putpixel( (i, j), (randint(0,255), randint(0,255), randint(0,255)))
        else:
            #grayscale mode
            im.putpixel( (i, j), randint(0,255))

#save image to unknown location
#im.save('simplePixel.png')

#pulls up image in default photo app
im.show()