from random import randint
from PIL import Image
from CommonAndUI import loadBar

with Image.open("OnMyWay.png") as im:
    width, height = im.size
    im.show()
im_new = Image.new('RGB', (width, height))

def blurPixel(i, j):
    blurred_pixel = []
    rAvg, gAvg, bAvg = 0, 0, 0
    if(i > 0 and i < width and j > 0 and j < height):
        for x_offset in range(-1,1):
            for y_offset in range(-1,1):
                rAvg += im.getpixel(i+x_offset, j+y_offset)[0]
                gAvg += im.getpixel(i+x_offset, j+y_offset)[1]
                bAvg += im.getpixel(i+x_offset, j+y_offset)[2]
        blurred_pixel.append(rAvg)
        blurred_pixel.append(gAvg)
        blurred_pixel.append(bAvg)
    
    blurred_pixel = tuple(blurred_pixel)
    print(blurred_pixel)
    return blurred_pixel
                


#print(width, height)
for i in range(width):
    for j in range(height):
        pixel = im.getpixel( (i, j) )
        im_new.putpixel( (i, j), blurPixel(i, j) )
    #print("Row", i, "is done")
    loadBar(iteration=i, total = width)


#save image to unknown location
#im.save('simplePixel.png')

#pulls up image in default photo app
im_new.show()