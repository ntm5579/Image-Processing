from random import randint
from PIL import Image

with Image.open("OnMyWay.png") as im:
    width, height = im.size
    im.show()

#print(width, height)

#negative
'''
for i in range(width):
    for j in range(height):
        pixel = im.getpixel( (i, j) )
        im.putpixel( (i, j), (255-pixel[0], 255-pixel[1], 255-pixel[2]))
'''

for i in range(width):
    print("Row", i, "is done")
    for j in range(height):
        pixel = im.getpixel( (i, j) )
        randomized_pixel = []
        for h in range(3):
            random_value = randint(-255,255)
            while pixel[h] + random_value < 255 and pixel[h] + random_value > 0:
                random_value = randint(-255, 255)
            randomized_pixel.append(pixel[h] + random_value)
        tuple(randomized_pixel)
        im.putpixel( (i, j), (randomized_pixel[0], randomized_pixel[1], randomized_pixel[2]) )


#save image to unknown location
#im.save('simplePixel.png')

#pulls up image in default photo app
im.show()