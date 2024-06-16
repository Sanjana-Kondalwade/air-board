import runpy
from tkinter import *

root =Tk()
root.geometry('300x300')
l = Label(root, text="Air Board")
l.pack()
def buttonFunction():
    runpy.run_path('air_canvas_ml.py')
b1= Button(root, text="air board",command=buttonFunction)
b1.pack()
def buttonFunction_2():
    runpy.run_path('gesture_presentation.py')
b2= Button(root, text="presentation",command=buttonFunction_2)
b2.pack()
root.mainloop()