from PIL import Image
from CommonAndUI import loadBar

with Image.open("TestImage2.png") as im:
    width, height = im.size
    im.show()
im_new = Image.new('RGB', (width, height))

def blurPixel(i, j):
    rAvg, gAvg, bAvg = 0, 0, 0

    xrangeList = [-1,1]
    yrangeList = [-1,1]
    if(i == 0):
        xrangeList = [0,1]
    if(j == 0):
        yrangeList = [0,1]
    if(i == width):
        xrangeList = [-1,0]
    if(j == height):
        yrangeList = [-1,0]
    
    for x_offset in range(xrangeList[0],xrangeList[1]):
        for y_offset in range(yrangeList[0],yrangeList[1]):
            targetPixel = im.getpixel((i+ x_offset, j+ y_offset))
            rAvg += targetPixel[0]
            gAvg += targetPixel[1]
            bAvg += targetPixel[2]
    self_sub = im.getpixel((i, j))
    rAvg -= self_sub[0]
    gAvg -= self_sub[1]
    bAvg -= self_sub[2]

    #divide by 8 because we are not taking into account the color of that pixel
    blurred_pixel = [rAvg//8, gAvg//8, bAvg//8]
    blurred_pixel = tuple(blurred_pixel)
    #print(blurred_pixel)
    return blurred_pixel
                


#print(width, height)
for i in range(width):
    for j in range(height):
        im_new.putpixel( (i, j), blurPixel(i, j) )
    #print("Row", i, "is done")
    loadBar(iteration=i, total = width)


#save image to unknown location
#im.save('simplePixel.png')

#pulls up image in default photo app
im_new.show()
