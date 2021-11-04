from tkinter import *
from tkinter.filedialog import askopenfilename, test
from Functions import *
from PIL import ImageTk, Image


menuList = []

def loadAndUnload(menuToLoad):
    for menu in menuList:
        if menu != menuToLoad:
            menu.grid_forget()
    menuToLoad.grid(column = 0, row= 0)

window = Tk()
window.geometry('800x600')
window.title("Gui Test")
window.resizable(False, False) 

#---------------------------------------------------------------------------
#holds the home and back button, displayed most of the time
universalFrame = Frame(window, width= 30, height = 2, bg= 'aqua')
universalFrame.grid(column= 1, row = 0, sticky= "NE")

#loads the last frame and then takes that item off of the list of pages, does not work rn, watch for minus two indexing issues
backButton = Button(universalFrame, text= "Back", width = 15, height = 2, command=lambda: loadAndUnload(previousWindow[-2]))
backButton.grid(column=0, row= 0, padx= 5, pady = 5)

homeButton = Button(universalFrame, text= "Home", width = 10, height = 2, command=lambda: loadAndUnload(mainMenu))
homeButton.grid(column=1, row= 0, padx= 5, pady = 5)

exitButton = Button(universalFrame, text= "Exit", width = 10, height = 2, command=window.quit)
exitButton.grid(column=1, row= 1, padx= 5, pady = 5)
#---------------------------------------------------------------------------

#the starting menu that lets you get to the create and upload pages
mainMenu = Frame(window)
mainMenu.grid(column = 0, row= 0, padx= 15)
menuList.append(mainMenu)

previousWindow = [mainMenu]

menuLabel = Label(mainMenu, text="Menu", width= 65, height= 2, bg = "Coral")
menuLabel.grid(column= 0, row= 0, padx= 10, columnspan=2)

uploadButton = Button(mainMenu, text= "Upload your own image", width = 20, height = 4, command= lambda:loadAndUnload(uploadMenu))
uploadButton.grid(column = 0, row= 1, padx= 5, pady = 10)

uploadMenu = Frame(window)
menuList.append(uploadMenu)

uploadLabel = Label(uploadMenu, text = "Uploading and shit", width= 65, height=2, bg = "Coral")
uploadLabel.grid(column = 0, row= 0, padx= 10, columnspan=2)

filename = ''
def imageUpload():
    global filename
    Tk().withdraw() # we don't want a full GUI, so keep the root window from appearing
    filepath = askopenfilename() # show an "Open" dialog box and return the path to the selected file
    if filepath != '':
        #print(filepath)
        blurButton.config(state='normal')
        scrambleButton.config(state='normal')
        #make this a preview of upload
        uploadedImageDisplay = Frame(uploadMenu, bg= 'aqua')
        uploadedImageDisplay.grid(column= 1, row = 1, padx= 5, pady = 5)
        fileNameLabel = Label(uploadedImageDisplay, text = filepath[:15] + '...' + filepath[-15:-1])
        fileNameLabel.grid(column= 0, row = 0)
        im = ImageTk.PhotoImage(Image.open(filepath))
        thumbNailIm = Canvas(uploadedImageDisplay, height= 100, width= 100)
        thumbNailIm.create_image(20, 20, image = im)
        thumbNailIm.grid(column= 0, row = 1)

#set up command to get a file path to work with, have this function enable the blurbutton and scramble button
uploadImageButton = Button(uploadMenu, text= "Upload an Image", width = 15, height = 2, command=imageUpload)
uploadImageButton.grid(column= 0, row = 1, padx= 5, pady = 5)

#hook this up to the blur func and pass argument of file path, enable when you get a file path
blurButton = Button(uploadMenu, text= "Blur this image", state="disabled", width = 20, height = 4, command= lambda:Blur(filename))
blurButton.grid(column= 0, row = 2, padx= 5, pady = 5)

scrambleButton = Button(uploadMenu, text= "Scramble this image", state="disabled", width = 20, height = 4, command= lambda:Scrambler(filename))
scrambleButton.grid(column= 1, row = 2, padx= 5, pady = 5)


createMenu = Frame(window)
menuList.append(createMenu)

createButton = Button(mainMenu, text="Create a new image", width = 20, height = 4, command=lambda: loadAndUnload(createMenu))
createButton.grid(column = 1, row= 1, padx= 5)

createLabel = Label(createMenu, text = "Creating and shit", width= 65, height= 2, bg = "coral")
createLabel.grid(column = 0, row= 0, padx= 5, columnspan=2)

numLabel = Label(createMenu, text= "Enter the size of square you would like to generate")
numLabel.grid(column= 0, row = 1, padx= 5, pady = 5, columnspan=2)

numField = Entry(createMenu)
numField.grid(column= 0, row = 2, padx= 5, pady = 5, columnspan=2)

numWarningLabel = Label(createMenu, text= "That is not a number")

def testInput(numFieldInput):
    if(numFieldInput.isdecimal()):
        NoiseGenerator(int(numFieldInput), rgb)
        print(rgb)
    else:
        numWarningLabel.grid(column= 0, row = 3, padx= 5, pady = 5, columnspan=2)

bwRgbLabel = Label(createMenu, text= "Would you like Black and White Noise or Noise with all colors?")
bwRgbLabel.grid(column= 0, row = 4, padx= 5, pady = 5, columnspan=2)

rgb = False

def switchBwRgb(mode):
    global rgb
    if mode == 'rgb':
        bwButton.config(state= 'normal')
        rgbButton.config(state= 'disabled')
        rgb = True
    else:    
        bwButton.config(state='disabled')
        rgbButton.config(state= 'normal')
        rgb = False

bwButton = Button(createMenu, text= "Black and White", width = 15, height = 2, state='disabled', command= lambda: switchBwRgb('bw'))
bwButton.grid(column= 0, row = 5, padx= 5, pady = 5)

rgbButton = Button(createMenu, text= "Rgb", width = 15, height = 2, command= lambda: switchBwRgb('rgb'))
rgbButton.grid(column= 1, row = 5, padx= 5, pady = 5)

noiseButton = Button(createMenu, text= "Make Some Noise", width = 60, height = 4, command= lambda: testInput(numField.get()))
noiseButton.grid(column= 0, row = 6, padx= 5, pady = 5, columnspan=2)

window.mainloop()