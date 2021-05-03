from tkinter import *
from PIL import ImageTk, Image
from tkinter import filedialog
import os

# Had to do pip install image
#what 
root = Tk()
root.geometry("550x300+700+200")
root.resizable(width=True, height=True)

def openfn():
    filename = filedialog.askopenfilename(title='open')
    return filename

def open_img():
    x = openfn()
    img = Image.open(x)
    img = img.resize((250, 250), Image.ANTIALIAS)
    img = ImageTk.PhotoImage(img)
    panel = Label(root, image=img)
    panel.image = img
    panel.pack()

def openTrainFile():
	file = filedialog.askopenfilename()

def beginTraining():
	return 0


topLabel = Label(root, text="GUI Project created by...")
trainBtn = Button(root, text='Training Folder', command=openTrainFile)
trainBtnStart = Button(root, text='Start Training..', command=beginTraining)


trainBtnStart.pack(side=BOTTOM, pady=10,)
topLabel.pack(pady=5,)
btn = Button(root, text='Image To Classify', command=open_img).pack(pady=10,)
trainBtn.pack(pady=10,)
root.mainloop()