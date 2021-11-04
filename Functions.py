from random import randint
from PIL import Image

#do not call without fixing input
#makes a square of rgb or bw noise size by size in dimensions.
def NoiseGenerator(size, rgb = False):
    #determines what mode the image is created in
    if rgb:
        #rgb mode
        im = Image.new('RGB', (size,size))
    else:
        #grayscale mode
        im = Image.new('L', (size,size))

    for i in range(size):
        for j in range(size):
            #rgb mode
            if rgb:
                #places pixels in new image with a randomized rgb values
                im.putpixel( (i, j), (randint(0,255), randint(0,255), randint(0,255)))
            #grayscale mode
            else:
                #places pixels in new image with a randomized w value
                im.putpixel( (i, j), randint(0,255))
    #diplays the finished image in photos app
    im.show()

#devitates each pixel rgb value a random amount from the original image
def Scrambler(filePath):
    #opens and assigns the image selected to im
    with Image.open(filePath).convert('RGB') as im:
        width, height = im.size
        #shows the image, needed for init rn, would like to remove
        #marked for removal
        im.show()
    
    #loops through x values
    for i in range(width):
        #loops through y values
        for j in range(height):
            #stores the rgb values of the current pixel being worked on
            pixel = im.getpixel( (i, j) )
            randomized_pixel = []
            #generates a random value for each color channel to deviate from the original pixel
            for h in range(3):
                random_value = randint(-255,255)
                #makes sure the new pixel value is displayable in rgb format (0-255), rerandomizes if not
                while pixel[h] + random_value < 255 and pixel[h] + random_value > 0:
                    random_value = randint(-255, 255)
                randomized_pixel.append(pixel[h] + random_value)
            #converts the randomized pixel to tuple to be placed on the new image
            randomized_pixel = tuple(randomized_pixel)
            im.putpixel( (i, j), randomized_pixel )
    im.show()

#makes a negative of the uploaded file
def makeNegative(filePath):
    with Image.open(filePath).convert('RGB') as im:
        width, height = im.size
        #marked for removal
        im.show()

    for i in range(width):
        for j in range(height):
            pixel = im.getpixel( (i, j) )
            #flips the pixel value by subtracting from max color value
            negativePixel = (255-pixel[0], 255-pixel[1], 255-pixel[2])
            im.putpixel( (i, j), negativePixel)

    im.show()

#add blurrer when it is finished
def Blur(filePath):
    print('Will blur Filepath', filePath, "when the method works")