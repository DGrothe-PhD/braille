
#!/usr/local/bin/python3
# -*- coding: utf8 -*-

# Written by Aadit Trivedi
# June 6, 2018
# Braille Library

# # Dependencies
# 1) sudo apt-get install pyaudio
# 3) sudo apt-get install espeak 
# 2) pip3 install SpeechRecognition
# 3) pip3 install numpy
# 4) pip3 install pillow
# 5) sudo apt-get install pytesseract
# 6) sudo apt-get install opencv-python
# 7) pip3 install opencv
# 8) pip3 install matplotlib

# Upload to GitHub

import numpy as np
import os
from PIL import Image
from pytesseract import image_to_string
import matplotlib.pyplot as plt
import PIL
from model import charToArray, asciicodes, brailles

ascii_braille = {}

arrayLength = len(asciicodes)
counter = 0

while counter < arrayLength:
    ascii_braille[asciicodes[counter]] = brailles[counter]
    counter = counter + 1

letterToImgPath = {
    "a": "images/a.png",
    "b": "images/b.png",
    "c": "images/c.png",
    "d": "images/d.png",
    "e": "images/e.png",
    "f": "images/f.png",
    "g": "images/g.png",
    "h": "images/h.png",
    "i": "images/i.png",
    "j": "images/j.png",
    "k": "images/k.png",
    "l": "images/l.png",
    "m": "images/m.png",
    "n": "images/n.png",
    "o": "images/o.png",
    "p": "images/p.png",
    "q": "images/q.png",
    "r": "images/r.png",
    "s": "images/s.png",
    "t": "images/t.png",
    "u": "images/u.png",
    "v": "images/v.png",
    "w": "images/w.png",
    "x": "images/x.png",
    "y": "images/y.png",
    "z": "images/z.png",
    " ": "images/void.png",
    "#": "images/number.png",
}

def addImages(list_im):
    imgs = [ PIL.Image.open(i) for i in list_im ]
    min_shape = sorted( [(np.sum(i.size), i.size ) for i in imgs])[0][1]
    imgs_comb = np.hstack( (np.asarray( i.resize(min_shape) ) for i in imgs ) )
    imgs_comb = PIL.Image.fromarray(imgs_comb)
    imgs_comb.save('output.jpg')  
def writeImage(b_string):
    images = []
    for letter in b_string:
        images.append(letterToImgPath[letter])
    addImages(images)    
    img = Image.open('output.jpg')
    img.show()
def writeText(b_string):
    final_string = ''
    for letters in b_string:
        final_string = final_string + ascii_braille[letters.lower()]
    print(final_string)

def textToBraille(text):
    final_string = ''
    for char in text:
        char = char.lower()
        if char in charToArray.keys():
            final_string += ascii_braille[char]
            print(char + " " + str(charToArray[char]))
    print(final_string)
    return final_string
    
    
def textToSpeech(text):
    if ((os.system("espeak '" + str(text) + "'")) != 0):
        print("Client error: system does not support text-to-audio // may need to download [espeak] command line package")
    
def brailleToTextArray(array):
    new_chars = ''
    for key in array:
        for a_key in charToArray:
            if charToArray[a_key] == key:
                new_chars = new_chars + str(a_key)
    print(new_chars)
    return new_chars
def brailleToSpeechArray(array):
    textToSpeech(brailleToTextArray(array))

def brailleToSpeechImg(imgs):
    for img in imgs:
        for chars in letterToImgPath:
            if img == letterToImgPath[chars]:
                print(chars)
def imageToText(img):
    return image_to_string(Image.open(img))
def imageToSpeech(img):
    textToSpeech(imageToText(img))
def imageToBraille(img):
    textToBraille(imageToText(img))


#imageToText("puretext.jpeg")