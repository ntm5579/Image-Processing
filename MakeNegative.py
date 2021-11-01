from random import randint
from PIL import Image
from GUI import loadBar

with Image.open("assets/TestImage1.png") as im:
    width, height = im.size
    im.show()

for i in range(width):
    for j in range(height):
        pixel = im.getpixel( (i, j) )
        im.putpixel( (i, j), (255-pixel[0], 255-pixel[1], 255-pixel[2]))

im.show()