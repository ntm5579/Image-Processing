from random import randint
from PIL import Image

#do not call without fixing input
def NoiseGenerator(size, rgb = False): #makes a square of rgb or bw noise size by size in dimensions.
    #determines what mode the image is created in
    if rgb: #rgb mode
        im = Image.new('RGB', (size,size))
    else: #grayscale mode
        im = Image.new('L', (size,size))

    for i in range(size): #loops through x values
        for j in range(size): #loops through y values
            if rgb: #rgb mode
                im.putpixel( (i, j), (randint(0,255), randint(0,255), randint(0,255))) #places pixels in new image with a randomized rgb values
            else: #grayscale mode
                im.putpixel( (i, j), randint(0,255)) #places pixels in new image with a randomized bw value
    im.show() #diplays the finished image in photos app

def Scrambler(filePath): #devitates each pixel rgb value a random amount from the original image
    with Image.open(filePath).convert('RGB') as im: #opens and assigns the image selected to im
        width, height = im.size
        #shows the image, needed for init rn, would like to remove
        im.show()#marked for removal
    
    for i in range(width): #loops through x values
        for j in range(height): #loops through y values
            pixel = im.getpixel( (i, j) )#stores the rgb values of the current pixel being worked on
            randomized_pixel = []
            for h in range(3): #generates a random value for each color channel to deviate from the original pixel
                random_value = randint(-255,255)
                while pixel[h] + random_value < 255 and pixel[h] + random_value > 0: #makes sure the new pixel value is displayable in rgb format (0-255), rerandomizes if not
                    random_value = randint(-255, 255)
                randomized_pixel.append(pixel[h] + random_value)
            randomized_pixel = tuple(randomized_pixel) #converts the randomized pixel to tuple to be placed on the new image
            im.putpixel( (i, j), randomized_pixel )
    im.show() #diplays the finished image in photos app

def makeNegative(filePath): #makes a negative of the uploaded file
    with Image.open(filePath).convert('RGB') as im:
        width, height = im.size
        im.show() #marked for removal

    for i in range(width): #loops through x values
        for j in range(height): #loops through y values
            pixel = im.getpixel( (i, j) )
            negativePixel = (255-pixel[0], 255-pixel[1], 255-pixel[2]) #flips the pixel value by subtracting from max color value
            im.putpixel( (i, j), negativePixel)
    im.show() #diplays the finished image in photos app

def Blur(filePath):
    #add body of blurrer when it is finished
    print('Will blur Filepath', filePath, "when the method works")