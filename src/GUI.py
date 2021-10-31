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
                menu.pack_forget()
        menuToLoad.pack()

    def loadPreviouswindow():
        loadAndUnload(previousWindow)

    window = Tk()
    window.geometry('600x400')
    window.title("Test")

    backButton = Button(window, text= "Back", command=lambda: loadAndUnload(previousWindow))
    backButton.pack()

    mainMenu = Frame(window)
    mainMenu.pack()
    menuList.append(mainMenu)

    previousWindow = mainMenu

    firstLabel = Label(mainMenu, text="Test")
    firstLabel.pack()

    uploadButton = Button(mainMenu, text= "Upload your own image", command= lambda:loadAndUnload(uploadMenu))
    uploadButton.pack()

    #think about init for items on the frames
    uploadMenu = Frame(window)
    menuList.append(uploadMenu)

    createMenu = Frame(window)
    menuList.append(createMenu)

    window.mainloop()

if __name__ == "__main__":
    GUI_Init()