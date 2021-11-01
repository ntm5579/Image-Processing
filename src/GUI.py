from tkinter import *

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
        menuToLoad.grid(column = 1, row= 1)

    window = Tk()
    window.geometry('600x400')
    window.title("Gui Test")

    #loads the last window and then takes that item off of the list of pages, watch the minus two indexing issus
    backButton = Button(window, text= "Back", command=lambda: loadAndUnload(previousWindow[-2]))
    backButton.grid(column=2, row= 0)

    homeButton = Button(window, text= "Home", command=lambda: loadAndUnload(mainMenu))
    homeButton.grid(column=3, row= 0)

    mainMenu = Frame(window)
    mainMenu.grid(column = 1, row= 1)
    menuList.append(mainMenu)

    previousWindow = [mainMenu]

    menuLabel = Label(mainMenu, text="Menu")
    menuLabel.grid(column=0, row= 0)

    uploadButton = Button(mainMenu, text= "Upload your own image", command= lambda:loadAndUnload(uploadMenu))
    uploadButton.grid(column = 0, row= 1)

    uploadMenu = Frame(window)
    menuList.append(uploadMenu)

    uploadLabel = Label(uploadMenu, text = "Uploading and shit")
    uploadLabel.grid(column = 0, row= 0)

    createMenu = Frame(window)
    menuList.append(createMenu)

    createButton = Button(mainMenu, text="Create a new image", command=lambda: loadAndUnload(createMenu))
    createButton.grid(column = 2, row= 1)

    createLabel = Label(createMenu, text = "Creating and shit")
    createLabel.grid(column = 0, row= 0)

    window.mainloop()

#prevents this Gui_Init from getting called on import of loadBar()
if __name__ == "__main__":
    GUI_Init()