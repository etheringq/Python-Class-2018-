from keras.applications.vgg16 import VGG16, preprocess_input, decode_predictions 
from keras.preprocessing import image
from PIL import Image
import matplotlib.pyplot as plt
import numpy as np
import sys

from tkinter import filedialog
from tkinter import *


def predict(filename, featuresize):
    img= image.load_img(filename, target_size=(224, 224))
    x = image.img_to_array(img)
    x = np.expand_dims(x, axis=0)
    preds= model.predict(preprocess_input(x))
    results = decode_predictions(preds, top=featuresize)[0]
    return results

def showimg(filename, title, i):
    im= Image.open(filename)
    im_list= np.asarray(im)
    plt.subplot(2, 5, i)
    plt.title(title)
    plt.axis("off")
    plt.imshow(im_list)
    
root = Tk()
text = Text(root)
text.insert(INSERT,"Cat vs Dog\n")
text.pack()

root.filename =  filedialog.askopenfilename(initialdir = "/",title = "Select file",filetypes = (("jpeg files","*.jpg"),("all files","*.*")))

plt.figure(figsize=(20, 10))
for i in range(1):
    showimg(root.filename, "query", i+1)
    plt.show()
    results = predict(root.filename, 10)
    for result in results:
        print(result)
        text.insert(INSERT,result)
        