from tkinter import filedialog
from tkinter import *

root = Tk()
text = Text(root)
text.insert(INSERT,"hello....\n")
text.pack()

root.filename =  filedialog.askopenfilename(initialdir = "/",title = "Select file",filetypes = (("jpeg files","*.jpg"),("all files","*.*")))

text.insert(INSERT,f'{str(root.filename)}')
text.pack()

root.mainloop()