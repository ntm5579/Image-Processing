from PIL import Image
from GUI import loadBar

with Image.open("assets/TestImage2.png").convert('RGB') as im:
    width, height = im.size
    im.show()

for i in range(width):
    for j in range(height):
        pixel = im.getpixel( (i, j) )
        negativePixel = (255-pixel[0], 255-pixel[1], 255-pixel[2])
        im.putpixel( (i, j), negativePixel)
    loadBar(i, width)

im.show()