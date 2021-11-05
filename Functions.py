from pathlib import WindowsPath
from random import randint
from PIL import Image
from math import sqrt

def rinseAndOpen(filepath):
    #print("Before: ", filepath)
    #make it so all escape characters have been removed
    for i in range(len(filepath)):
        #print('index:', i, 'Char:', filepath[i])
        if(filepath[i] == "\\"):
            filepath = filepath[:i] + '/' + filepath[i + 1:]
        elif(filepath[i] == "\n"):
            filepath = filepath[:i] + '/n' + filepath[i + 1:]
        elif(filepath[i] == "\r"):
            filepath = filepath[:i] + '/r' + filepath[i + 1:]
        elif(filepath[i] == "\t"):
            filepath = filepath[:i] + '/t' + filepath[i + 1:]
        elif(filepath[i] == "\b"):
            filepath = filepath[:i] + '/b' + filepath[i + 1:]
        elif(filepath[i] == "\f"):
            filepath = filepath[:i] + '/f' + filepath[i + 1:]
        elif(filepath[i] == "\a"):
            filepath = filepath[:i] + '/a' + filepath[i + 1:]
    #print("After:", filepath)
    with Image.open(r"{s}".format(s = filepath)).convert('RGB') as im: #opens and assigns the image selected to im
        #shows the image, needed for init rn, would like to remove
        im.show()#marked for removal
    return im

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

def NoiseClusters(size, r = 10, numClusters = -1): #makes a square of rgb or bw noise size by size in dimensions.
    hotspots = []
    if(numClusters < 0):
        for _ in range(randint(5,20)):
            newHotSpot = (randint(0,size), randint(0,size))
            while hotspots.count(newHotSpot) > 0:
                newHotSpot = (randint(0,size), randint(0,size))
            hotspots.append(newHotSpot)
    else:
        for _ in range(numClusters):
            newHotSpot = (randint(0,size), randint(0,size))
            while hotspots.count(newHotSpot) > 0:
                newHotSpot = (randint(0,size), randint(0,size))
            hotspots.append(newHotSpot)
    #print(hotspots)

    im = Image.new('L', (size,size))
    for i in range(size):
        for j in range(size):
            im.putpixel( (i, j), (255) )
    #add a way to check if points are in the boundaries of other clusters, avearge the values then
    overlap = []
    for points in hotspots:
        for x_offset in range(-r,r):
            for y_offset in range(-r,r):
                distance = int(sqrt((x_offset) ** 2 + (y_offset) ** 2))
                if(distance < r):
                    color = (int(distance/sqrt( r**2 + r**2) * 255))
                    try:
                        im.putpixel( (points[0] + x_offset, points[1] + y_offset), color )
                    except IndexError:
                        break

    im.show()
            
#NoiseClusters(500, r = 100)

#open does not work when taking full file path from windows file select
def Scrambler(filePath): #devitates each pixel rgb value a random amount from the original image
    im = rinseAndOpen(filePath)
    width, height = im.size
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
    im = rinseAndOpen(filePath)
    width, height = im.size
    for i in range(width): #loops through x values
        for j in range(height): #loops through y values
            pixel = im.getpixel( (i, j) )
            negativePixel = (255-pixel[0], 255-pixel[1], 255-pixel[2]) #flips the pixel value by subtracting from max color value
            im.putpixel( (i, j), negativePixel)
    im.show() #diplays the finished image in photos app

def Blur(filePath):
    im = rinseAndOpen(filePath)
    width, height = im.size
    #add body of blurrer when it is finished
    print('Will blur Filepath', filePath, "when the method works")