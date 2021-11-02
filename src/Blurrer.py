from PIL import Image
from GUI import loadBar

with Image.open("assets/TestImage2.png").convert('RGB') as im:
    width, height = im.size
    #removing this causes an error
    im.show()
im_new = Image.new('RGB', (width, height))

def blurPixel(i, j):
    rAvg, gAvg, bAvg = 0, 0, 0

    xrangeList = [-1,2]
    yrangeList = [-1,2]
    if(i == 0):
        xrangeList = [0,2]
    if(j == 0):
        yrangeList = [0,2]
    if(i == width):
        xrangeList = [-1,0]
    if(j == height):
        yrangeList = [-1,0]

    for x_offset in range(xrangeList[0], xrangeList[1]):
        for y_offset in range(yrangeList[0], yrangeList[1]):
            try:
                targetPixel = im.getpixel((i+ x_offset, j+ y_offset))
            except IndexError:
                print('i', i , 'j', j)
                exit()
            rAvg += targetPixel[0]
            gAvg += targetPixel[1]
            bAvg += targetPixel[2]

    #divide by 8 because we are not taking into account the color of that pixel
    blurred_pixel = [rAvg//9, gAvg//9, bAvg//9]
    blurred_pixel = tuple(blurred_pixel)
    return blurred_pixel

#print(width, height)
for i in range(width - 1):
    for j in range(height - 1):
        im_new.putpixel( (i, j), blurPixel(i, j) )
    loadBar(iteration=i, total = width)

im_new.show()