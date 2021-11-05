from PIL import Image
from Functions import rinseFilePath

filePath = "D:\Coding\Projects by Language\Python Projects\Image Processing\assets\TestImage2.png"
#print('len:', len(filePath))
filePath = rinseFilePath(filePath)
with Image.open(r"{s}".format(s = filePath)).convert('RGB') as im: #opens and assigns the image selected to im
        width, height = im.size
        #shows the image, needed for init rn, would like to remove
        im.show()#marked for removal