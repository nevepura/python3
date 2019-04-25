from sys import version_info
if version_info.major == 2:
    # Python 2.x
    from Tkinter import *
    from Tkinter.ttk import *


elif version_info.major == 3:
    # Python 3.x
    from tkinter import *
    from tkinter.ttk import *

app = Tk()
l = Label (app, text= "i am a label")
b = Button (app, text = "best button")

l.text = "i was a label"


l.pack()
b.pack()
app.mainloop()
