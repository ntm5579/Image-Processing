from random import randint
from PIL import Image

#do not call without fixing input
def NoiseGenerator(size, rgb = False):
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
    im.show()

#handle image input, might have to 
def Scrambler(filePath):
    with Image.open(filePath).convert('RGB') as im:
        width, height = im.size
        im.show()
    width, height = im.size
    for i in range(width):
        #print("Row", i, "is done")
        for j in range(height):
            pixel = im.getpixel( (i, j) )
            randomized_pixel = []
            for h in range(3):
                random_value = randint(-255,255)
                while pixel[h] + random_value < 255 and pixel[h] + random_value > 0:
                    random_value = randint(-255, 255)
                randomized_pixel.append(pixel[h] + random_value)
            randomized_pixel = tuple(randomized_pixel)
            im.putpixel( (i, j), randomized_pixel )
        #loadBar(iteration=i, total = width)
    im.show()

def makeNegative(filePath):
    with Image.open(filePath).convert('RGB') as im:
        width, height = im.size
        im.show()

    for i in range(width):
        for j in range(height):
            pixel = im.getpixel( (i, j) )
            negativePixel = (255-pixel[0], 255-pixel[1], 255-pixel[2])
            im.putpixel( (i, j), negativePixel)
        #loadBar(i, width)

    im.show()

#add blurrer when it is finished