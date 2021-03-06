from tkinter import *
from tkinter.filedialog import askopenfilename, test
from Functions import *
from PIL import ImageTk, Image
import threading


menuList = []

def loadAndUnload(menuToLoad, remove = False):
    global previousWindow
    if(remove == False):
        previousWindow.append(menuToLoad)
    else:
        previousWindow.pop(-2)
    
    if(menuToLoad == mainMenu):
        previousWindow = [mainMenu]
        backButton.config(state='disable')
    else:
        backButton.config(state='normal')
    
    for menu in menuList:
        if menu != menuToLoad:
            menu.grid_forget()
    menuToLoad.grid(column = 0, row= 1, padx= 15, pady = 5)

window = Tk()
window.geometry('500x400')
window.title("Image Processor")
window.resizable(False, False)
window.config(bg='dark gray')

#---------------------------------------------------------------------------
universalFrame = Frame(window, width= 100, height = 2, bg= 'aqua') #holds the home and back button, displayed most of the time
universalFrame.grid(column= 0, row = 0, padx= 15, pady = 5, columnspan=3)

homeButton = Button(universalFrame, text= "Home", width = 10, height = 2, command=lambda: loadAndUnload(mainMenu))
homeButton.grid(column=0, row= 0, padx= 5, pady = 5)

#loads the last frame and then takes that item off of the list of pages, does not work rn, watch for minus two indexing issues
backButton = Button(universalFrame, text= "Back", width = 15, height = 2, state='disabled', command=lambda: loadAndUnload(previousWindow[-2], True))
backButton.grid(column=1, row= 0, padx= 5, pady = 5)

settingsButton = Button(universalFrame, text= "Settings", width = 10, height = 2)
#settingsButton.grid(column=2, row= 0, padx= 5, pady = 5)

exitButton = Button(universalFrame, text= "Exit", width = 10, height = 2, command=window.quit)
exitButton.grid(column=3, row= 0, padx= 5, pady = 5)
#---------------------------------------------------------------------------

#the starting menu that lets you get to the create and upload pages
mainMenu = Frame(window, bg= 'white')
mainMenu.grid(column = 0, row= 1, padx= 15, pady=5)
menuList.append(mainMenu)

previousWindow = [mainMenu]

menuLabel = Label(mainMenu, text="Menu", width= 65, height= 2, bg = "Coral")
menuLabel.grid(column= 0, row= 0, padx= 5, pady = 5, columnspan=2)

uploadButton = Button(mainMenu, text= "Upload your own image", width = 20, height = 4, command= lambda:loadAndUnload(uploadMenu))
uploadButton.grid(column = 0, row= 1, padx= 5, pady = 10)

uploadMenu = Frame(window, bg= 'white')
menuList.append(uploadMenu)

uploadLabel = Label(uploadMenu, text = "Uploading and shit", width= 65, height=2, bg = "Coral")
uploadLabel.grid(column = 0, row= 0, padx= 5, pady= 5, columnspan=3)

filepath = ''
def imageUpload():
    global filepath
    Tk().withdraw() # we don't want a full GUI, so keep the root window from appearing
    filepath = askopenfilename() # show an "Open" dialog box and return the path to the selected file
    if filepath != '':
        #print(filepath)
        scrambleButton.config(state='normal')
        negativeButton.config(state='normal')
        #make this a preview of upload

        fileNameLabel = Label(uploadMenu, text = filepath[:20] + '...' + filepath[-20:-1] + filepath[-1])
        fileNameLabel.grid(column= 1, row = 1, columnspan=2)
        '''
        im = ImageTk.PhotoImage(Image.open(filepath))
        thumbNailIm = Canvas(uploadedImageDisplay, height= 100, width= 100)
        thumbNailIm.create_image(20, 20, image = im)
        thumbNailIm.grid(column= 0, row = 1)
        '''

#set up command to get a file path to work with, have this function enable the blurbutton and scramble button
uploadImageButton = Button(uploadMenu, text= "Upload an Image", width = 15, height = 2, command=imageUpload)
uploadImageButton.grid(column= 0, row = 1, padx= 5, pady = 5)

scrambleButton = Button(uploadMenu, text= "Scramble this image", state="disabled", width = 30, height = 4, command= threading.Thread(target=lambda:Scrambler(filepath)).start)
scrambleButton.grid(column= 0, row = 2, padx= 5, pady = 5, columnspan=2)

negativeButton = Button(uploadMenu, text= "Make a negative", state="disabled", width = 30, height = 4, command= threading.Thread(target=lambda:makeNegative(filepath)).start)
negativeButton.grid(column= 2, row = 2, padx= 5, pady = 5, columnspan=2)

createMenu = Frame(window, bg= 'white')
menuList.append(createMenu)

createButton = Button(mainMenu, text="Create a new image", width = 20, height = 4, command= lambda:loadAndUnload(createMenu))
createButton.grid(column = 1, row= 1, padx= 5)

createLabel = Label(createMenu, text = "Creating and shit", width= 65, height= 2, bg = "coral")
createLabel.grid(column = 0, row= 0, padx= 5, pady = 5, columnspan=2)

individualNoiseMenu = Frame(window)
menuList.append(individualNoiseMenu)

individualButton = Button(createMenu,text = "Individual Noise", width=20, height= 2, command= lambda:loadAndUnload(individualNoiseMenu))
individualButton.grid(column= 0, row = 1, padx= 5, pady = 5)

indivLabel = Label(individualNoiseMenu, text = "Indivual Noise Generation", width= 65, height= 2, bg = "coral")
indivLabel.grid(column = 0, row= 0, padx= 5, pady = 5, columnspan=2)

inNumLabel = Label(individualNoiseMenu, text= "Enter the size of square you would like to generate")
inNumLabel.grid(column= 0, row = 1, padx= 5, pady = 5, columnspan=2)

inNumField = Entry(individualNoiseMenu)
inNumField.grid(column= 0, row = 2, padx= 5, pady = 5, columnspan=2)

inNumWarningLabel = Label(individualNoiseMenu, fg = 'red', text= "That is not a number")

def testInput(numFieldInput):
    if(numFieldInput.isdecimal()):
        NoiseGenerator(int(numFieldInput), rgb)
    else:
        inNumWarningLabel.grid(column= 0, row = 3, padx= 5, pady = 5, columnspan=2)
        
bwRgbLabel = Label(individualNoiseMenu, text= "Would you like Black and White Noise or Noise with all colors?")
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

bwButton = Button(individualNoiseMenu, text= "Black and White", width = 15, height = 2, state='disabled', command= lambda: switchBwRgb('bw'))
bwButton.grid(column= 0, row = 5, padx= 5, pady = 5)

rgbButton = Button(individualNoiseMenu, text= "Rgb", width = 15, height = 2, command= lambda: switchBwRgb('rgb'))
rgbButton.grid(column= 1, row = 5, padx= 5, pady = 5)

inNoiseButton = Button(individualNoiseMenu, text= "Make Some Noise", width = 60, height = 4, command= threading.Thread(target=lambda:testInput(inNumField.get())).start)
inNoiseButton.grid(column= 0, row = 6, padx= 5, pady = 5, columnspan=2)

#-------------------------------------------------
clusterNoiseMenu = Frame(window)
menuList.append(clusterNoiseMenu)

clusterButton = Button(createMenu,text = "Clustered Noise", width=20,  height= 2, command=lambda:loadAndUnload(clusterNoiseMenu))
clusterButton.grid(column= 1, row = 1, padx= 5, pady = 5)

clusterLabel = Label(clusterNoiseMenu, text = "Cluster Noise Generation", width= 65, height= 2, bg = "coral")
clusterLabel.grid(column = 0, row= 0, padx= 5, pady = 5, columnspan=2)

clusResLabel = Label(clusterNoiseMenu, text= "Image Size")
clusResLabel.grid(column= 0, row = 1, padx= 5, pady = 5, columnspan=2)

clusResEntry = Entry(clusterNoiseMenu)
clusResEntry.grid(column= 0, row = 2, padx= 5, pady = 5, columnspan=2)

clusRadLabel = Label(clusterNoiseMenu, text= "Cluster Radius")
clusRadLabel.grid(column= 0, row = 3, padx= 5, pady = 5, columnspan=2)

clusRadEntry = Entry(clusterNoiseMenu)
clusRadEntry.grid(column= 0, row = 4, padx= 5, pady = 5, columnspan=2)

clusNumLabel = Label(clusterNoiseMenu, text= "Number of Clusters")
clusNumLabel.grid(column= 0, row = 5, padx= 5, pady = 5, columnspan=2)

clusNumEntry = Entry(clusterNoiseMenu)
clusNumEntry.grid(column= 0, row = 6, padx= 5, pady = 5, columnspan=2)

clusNumWarningLabel = Label(clusterNoiseMenu, fg = 'red', text= "There was an issue with your input, make sure there are no spaces\n and there are three elements seperated by commas")

clusNoiseButton = Button(clusterNoiseMenu, text= "Make Some Noise", width = 60, height = 4, command= threading.Thread(target=lambda: NoiseClusters(int(clusResEntry.get()), int(clusRadEntry.get()), int(clusNumEntry.get()))).start)
clusNoiseButton.grid(column= 0, row = 7, padx= 5, pady = 5, columnspan=2)
#-------------------------------------------------

window.mainloop()