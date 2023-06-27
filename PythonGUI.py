from tkinter import *

window  = Tk() #instantiate an instance of a window
window.geometry("420x420") #set the size of the window
window.title("LearningPY_GUI") #set the title of the window

AppIcon = PhotoImage(file='AppLogoNew.png') #change the icon of the window
window.iconphoto(True, AppIcon)
window.config(background="darkgrey")
window.config(format(image_names(time)))
window.mainloop() #place window on screen





























