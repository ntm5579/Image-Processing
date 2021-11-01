from tkinter import *
from Functions import *

#loadBar from Tyler Luedtke https://www.youtube.com/watch?v=MtYOrIwW1FQ
def loadBar(iteration, total, prefix='', suffix='', decimals=1,length=100, fill='>'):
    #this lihne might be wront
    percent = ('{0:.' + str(decimals) + 'f}').format(100 * (iteration/float(total)))
    filledLength = int(length * iteration // total)
    bar = fill * filledLength + "-" * (length - filledLength)
    print(f'\r{prefix} |{bar}| {percent}% {suffix}', end= '\r')
    if iteration == total:
        print()

def GUI_Init():
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

    universalFrame = Frame(window, width= 30, height = 2, bg= 'aqua')
    universalFrame.grid(column= 1, row = 0, sticky= "NE")

    #loads the last window and then takes that item off of the list of pages, watch the minus two indexing issus
    backButton = Button(universalFrame, text= "Back", width = 15, height = 2, command=lambda: loadAndUnload(previousWindow[-2]))
    backButton.grid(column=0, row= 0, padx= 5, pady = 5)

    homeButton = Button(universalFrame, text= "Home", width = 10, height = 2, command=lambda: loadAndUnload(mainMenu))
    homeButton.grid(column=1, row= 0, padx= 5, pady = 5)

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

    #set up command to get a file path to work with, have this function enable the blurbutton and scramble button
    uploadImageButton = Button(uploadMenu, text= "Click hear to upload \n an Image", width = 20, height = 4)
    uploadImageButton.grid(column= 0, row = 1, columnspan=2, padx= 5, pady = 5)

    #hook this up to the blur func and pass argument of file path, enable when you get a file path
    blurButton = Button(uploadMenu, text= "Click hear to upload \n an Image", state="disabled", width = 20, height = 4)
    blurButton.grid(column= 0, row = 2, padx= 5, pady = 5)

    scrambleButton = Button(uploadMenu, text= "Click hear to upload \n an Image", state="disabled", width = 20, height = 4)
    scrambleButton.grid(column= 1, row = 2, padx= 5, pady = 5)
    

    createMenu = Frame(window)
    menuList.append(createMenu)

    createButton = Button(mainMenu, text="Create a new image", width = 20, height = 4, command=lambda: loadAndUnload(createMenu))
    createButton.grid(column = 1, row= 1, padx= 5)

    createLabel = Label(createMenu, text = "Creating and shit", width= 65, height= 2, bg = "coral")
    createLabel.grid(column = 0, row= 0, padx= 5)

    noiseButton = Button(createMenu, text= "Make Some Noise", width = 60, height = 4)
    noiseButton.grid(column= 0, row = 2, padx= 5, pady = 5)

    window.mainloop()

#prevents this Gui_Init from getting called on import of loadBar()
if __name__ == "__main__":
    GUI_Init()