from PIL import Image

#loadBar from Tyler Luedtke https://www.youtube.com/watch?v=MtYOrIwW1FQ
def loadBar(iteration, total, prefix='', suffix='', decimals=1,length=100, fill='>'):
    #this lihne might be wront
    percent = ('{0:.' + str(decimals) + 'f}').format(100 * (iteration/float(total)))
    filledLength = int(length * iteration // total)
    bar = fill * filledLength + "-" * (length - filledLength)
    print(f'\r{prefix} |{bar}| {percent}% {suffix}', end= '\r')
    if iteration == total:
        print()

#refactor to make the whole thing a method
def blurPixel():
    weight_diag = 0.0947416
    weight_hv = 0.118318
    weight_self = 0.147761
    gaussian_values = [[weight_diag, weight_hv, weight_diag],[weight_hv, weight_self, weight_hv],[weight_diag, weight_hv, weight_diag]]

    with Image.open("assets/TestImage2.png").convert('RGB') as im:
        width, height = im.size
        #removing this causes an error
        im.show()
    im_new = Image.new('RGB', (width, height))

    for i in range(width - 1):
        for j in range(height - 1):
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
            #Gaussian Blur Algorithim https://www.pixelstech.net/article/1353768112-Gaussian-Blur-Algorithm
            for x_offset in range(xrangeList[0], xrangeList[1]):
                for y_offset in range(yrangeList[0], yrangeList[1]):
                    #remove try and except when the method is error free
                    try:
                        targetPixel = im.getpixel((i+ x_offset, j+ y_offset))
                    except IndexError:
                        print('i', i , 'j', j)
                        exit()
                    rAvg += int(targetPixel[0] * gaussian_values[x_offset][y_offset])
                    gAvg += int(targetPixel[1] * gaussian_values[x_offset][y_offset])
                    bAvg += int(targetPixel[2] * gaussian_values[x_offset][y_offset])
            
            #divide by 8 because we are not taking into account the color of that pixel
            #blurred_pixel = [rAvg//9, gAvg//9, bAvg//9]
            blurred_pixel = [rAvg, gAvg, bAvg]
            blurred_pixel = tuple(blurred_pixel)

            im_new.putpixel( (i, j), blurred_pixel )
        loadBar(i, width)
    im_new.show()