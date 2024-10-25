import random
import json
import torch
import os
import nltk
import sys
from Brain import NeuralNet
import pyautogui as p
from GreetMe import greetMe
from NeuralNetwork import NLPProcessor
from Task import NonInputExecution,InputExecution_ms_word,rememberExecution,temperatureExecution,GoogleMaps,My_loc,youtube_auto,Generate_Images,ShowImages,InputExecution_ms_ppt,wiki
from PyQt5 import QtGui
from time import time as t

import pyautogui
from PyQt5.QtCore import * 
from keyboard import press_and_release
from PyQt5.QtGui import * 
from PyQt5.QtWidgets import * 
from enablemateUi import Ui_enablemateUi
nlp_processor = NLPProcessor()
import cv2
from Listen import Listen
from Speak import speak

import warnings
warnings.filterwarnings("ignore", category=DeprecationWarning)
class MainThread(QThread):
    def __init__(self):
        super(MainThread, self).__init__()
    def run(self):
        self.TaskExecution()
    def TaskExecution(self):
        p.press('esc')
        greetMe()
        device=torch.device('cuda' if torch.cuda.is_available() else 'cpu') 
        file =open(os.path.join(sys.path[0], "intents.json"), "r")
        intents = json.load(file)
        FILE="TrainData.pth"
        data = torch.load(FILE, weights_only=True)
        input_size=data["input_size"]
        hidden_size=data["hidden_size"]
        output_size=data["output_size"]
        all_words=data["all_words"]
        tags=data["tags"]  
        model_state=data["model_state"]   
        model=NeuralNet(input_size,hidden_size,output_size).to(device)
        model.load_state_dict(model_state) 
        model.eval()
        while True:
            self.sentence1=Listen()
            
            if self.sentence1=="bye":
                exit()
            self.sentence=nlp_processor.tokenize(self.sentence1)
            X=nlp_processor.bag_of_words(self.sentence,all_words)
            X=X.reshape(1,X.shape[0])
            X=torch.from_numpy(X).to(device)
            output=model(X) 
            _,predicted=torch.max(output,dim=1) 
            tag=tags[predicted.item()]  
            probs=torch.softmax(output,dim=1)
            predicted_index = predicted.item()
            prob=probs[0,predicted_index]    
            if prob.item()>0.75:
                for intent in intents["intents"]:
                    if tag==intent["tag"]:
                        self.reply=random.choice(intent["responses"]) 
                        if "time" in self.reply:
                            NonInputExecution(self.reply)
                        elif "date" in self.reply:
                            NonInputExecution(self.reply)
                        elif "internet speed" in self.reply:
                            NonInputExecution(self.reply)
                        elif "remember that" in self.reply:
                            rememberExecution(self.reply,self.sentence1)
                        elif "what do you remember" in self.reply:
                            rememberExecution(self.reply,self.sentence1)
                        elif "clear remember file" in self.reply:
                            rememberExecution(self.reply,self.sentence1)
                        elif "temperature in" in self.reply:
                            temperatureExecution(self.reply,self.sentence1)
                        elif 'wikipedia' in self.reply:
                            wiki(self.sentence1)
                        elif "directions" in self.reply:
                            GoogleMaps(self.reply,self.sentence1)
                        elif "my location" in self.reply:
                            My_loc(self.reply)
                        elif "generate an image of" in self.reply:
                            Generate_Images(self.reply,self.sentence1)
                        elif "show images" in self.reply:
                            current_index = 0
                            while True:
                                if "show images" in self.reply:
                                    speak("Do you want to see images?: ")
                                    user_reply = Listen().lower() 
                                    if user_reply == 'yes please':
                                        success, current_index = ShowImages(self.reply, current_index) 
                                        if not success:
                                            speak("No more images to show.")
                                            
                                    elif user_reply == 'no thank you':
                                        speak("Okay, not showing images.")
                                        break  
                                    else:
                                        speak("Invalid response. Please enter 'yes' or 'no'.")
                        elif 'on youtube' in self.reply:
                            youtube_auto(self.sentence1)
                        elif 'pause' in tag:
                            press_and_release('k')
                        elif 'play' in tag:
                            press_and_release('k')
                        elif 'mute' in tag:
                            press_and_release('m')
                        elif 'unmute' in tag:
                            press_and_release('m')
                        elif 'next video' in tag:
                            press_and_release('shift + n')
                        elif 'previous video' in tag:
                            press_and_release('shift + p')
                        elif 'open miniplayer' in tag:
                            press_and_release('i')

                        elif 'caption' in tag:
                            press_and_release('c')

                        elif 'speed up' in tag:
                            press_and_release('shift + >')

                        elif 'slow down' in tag:
                            press_and_release('shift + <')

                        elif 'forward' in tag:
                            press_and_release('l')

                        elif 'backward' in tag:
                            press_and_release('j')
                        elif 'full screen' in tag:
                            
                            press_and_release('f')
                        elif "word" in self.reply:
                            InputExecution_ms_word(self.reply,self.sentence1)
                        elif "start writing" in self.reply:
                            InputExecution_ms_word(self.reply,self.sentence1)
                        elif "close document" in self.reply:
                            InputExecution_ms_word(self.reply,self.sentence1)
                        elif "align left" in self.reply:
                            InputExecution_ms_word(self.reply,self.sentence1)
                        elif "align centre" in self.reply:
                            InputExecution_ms_word(self.reply,self.sentence1)
                        elif "align right" in self.reply:
                            InputExecution_ms_word(self.reply,self.sentence1)
                        elif "justify" in self.reply:
                            InputExecution_ms_word(self.reply,self.sentence1)
                        elif "scroll down" in self.reply:
                            InputExecution_ms_word(self.reply,self.sentence1)
                        elif "select the previous word" in self.reply:
                            InputExecution_ms_word(self.reply,self.sentence1)
                        elif "select the next paragraph" in self.reply:
                            InputExecution_ms_word(self.reply,self.sentence1)
                        elif "select all text" in self.reply:
                            InputExecution_ms_word(self.reply,self.sentence1)
                        elif "deselect everything" in self.reply:
                            InputExecution_ms_word(self.reply,self.sentence1)  
                        elif "find" in self.reply:
                            InputExecution_ms_word(self.reply,self.sentence1)
                        elif "replace" in self.reply:
                            InputExecution_ms_word(self.reply,self.sentence1) 
                        elif "start spell check" in self.reply:
                            InputExecution_ms_word(self.reply,self.sentence1)
                        elif "ignore this word" in self.reply:
                            InputExecution_ms_word(self.reply,self.sentence1)
                        elif "change misspelled to corrected" in self.reply:
                            InputExecution_ms_word(self.reply,self.sentence1)
                        # Lists and Bullets
                        elif "start numbered list" in self.reply:
                            InputExecution_ms_word(self.reply,self.sentence1)
                    #font formatting
                        elif "increase font size" in self.reply:
                            InputExecution_ms_word(self.reply,self.sentence1) 
                        elif "bold text" in self.reply:
                            InputExecution_ms_word(self.reply,self.sentence1)
                        elif "italicize this" in self.reply:
                            InputExecution_ms_word(self.reply,self.sentence1)
                        elif "underline the selected text" in self.reply:
                            InputExecution_ms_word(self.reply,self.sentence1)
                        elif "change font to arial" in self.reply:
                            InputExecution_ms_word(self.reply,self.sentence1)
                        elif "change font to times new roman" in self.reply:
                            InputExecution_ms_word(self.reply,self.sentence1)
                        elif "change font size to 12" in self.reply:
                            InputExecution_ms_word(self.reply,self.sentence1)
                        elif "change font size to 16" in self.reply:
                            InputExecution_ms_word(self.reply,self.sentence1)
                    #text formatting
                        elif "cut this" in self.reply:
                            InputExecution_ms_word(self.reply,self.sentence1)
                        elif "copy the selection" in self.reply:
                            InputExecution_ms_word(self.reply,self.sentence1)
                        elif "paste" in self.reply:
                            InputExecution_ms_word(self.reply,self.sentence1)
                        elif "undo the last action" in self.reply:
                            InputExecution_ms_word(self.reply,self.sentence1)
                        elif "redo" in self.reply:
                            InputExecution_ms_word(self.reply,self.sentence1)
                        elif "go to the beginning of the line" in self.reply:
                            InputExecution_ms_word(self.reply,self.sentence1)
                        elif "go to the end of the document" in self.reply:
                            InputExecution_ms_word(self.reply,self.sentence1) 
                        elif "format the table" in self.reply:
                            InputExecution_ms_word(self.reply,self.sentence1)
                        elif "format the image" in self.reply:
                            InputExecution_ms_word(self.reply,self.sentence1)
                        elif "change background color to yellow" in self.reply:
                            InputExecution_ms_word(self.reply,self.sentence1)
                        elif "highlight selected text" in self.reply:
                            InputExecution_ms_word(self.reply,self.sentence1)
                        elif "add borders to selection" in self.reply:
                            InputExecution_ms_word(self.reply,self.sentence1)
                        elif "set table borders" in self.reply:
                            InputExecution_ms_word(self.reply,self.sentence1)
                        elif "apply table style" in self.reply:
                            InputExecution_ms_word(self.reply,self.sentence1)
                        elif "change cell background color" in self.reply:
                            InputExecution_ms_word(self.reply,self.sentence1)
                        elif "change text color" in self.reply:
                            InputExecution_ms_word(self.reply,self.sentence1)
                        elif "adjust column width" in self.reply:
                            InputExecution_ms_word(self.reply,self.sentence1)
                        elif "adjust row height" in self.reply:
                            InputExecution_ms_word(self.reply,self.sentence1)
                        elif "merge cells" in self.reply:
                            InputExecution_ms_word(self.reply,self.sentence1)
                        elif "split cells" in self.reply:
                            InputExecution_ms_word(self.reply,self.sentence1)
                        #insertion of image      
                        elif "insert an image from file" in self.reply:
                            InputExecution_ms_word(self.reply,self.sentence1)
                        #formatting of image        
                        elif "format the image" in self.reply:
                            InputExecution_ms_word(self.reply,self.sentence1)
                        elif "set image border" in self.reply:
                            InputExecution_ms_word(self.reply,self.sentence1)
                        elif "change image size" in self.reply:
                            InputExecution_ms_word(self.reply,self.sentence1)
                        elif "crop the image" in self.reply:
                            InputExecution_ms_word(self.reply,self.sentence1)
                        elif "apply image effects" in self.reply:
                            InputExecution_ms_word(self.reply,self.sentence1)
                        elif "rotate the image" in self.reply:
                            InputExecution_ms_word(self.reply,self.sentence1)
                        elif "change image brightness" in self.reply:
                            InputExecution_ms_word(self.reply,self.sentence1)
                        elif "adjust image contrast" in self.reply:
                            InputExecution_ms_word(self.reply,self.sentence1)
                        elif "compress the image" in self.reply:
                            InputExecution_ms_word(self.reply,self.sentence1)
                        elif "reset image formatting" in self.reply:
                            InputExecution_ms_word(self.reply,self.sentence1)              
                    #insertion of list,hyperlink and shapes
                        elif "create a bulleted list" in self.reply:
                            InputExecution_ms_word(self.reply,self.sentence1)
                        elif "add a comment here" in self.reply:
                            InputExecution_ms_word(self.reply,self.sentence1)
                        elif "insert a hyperlink" in self.reply:
                            InputExecution_ms_word(self.reply,self.sentence1)   
                        elif "insert a rectangle shape" in self.reply:
                            InputExecution_ms_word(self.reply,self.sentence1)
                        elif "insert an oval shape" in self.reply:
                            InputExecution_ms_word(self.reply,self.sentence1)
                        elif "insert a triangle shape" in self.reply:
                            InputExecution_ms_word(self.reply,self.sentence1)
                        elif "insert a star shape" in self.reply:
                            InputExecution_ms_word(self.reply,self.sentence1)
                        elif "insert a line shape" in self.reply:
                            InputExecution_ms_word(self.reply,self.sentence1)
                        elif "insert a callout shape" in self.reply:
                            InputExecution_ms_word(self.reply,self.sentence1)
                        elif "change background color to yellow" in self.reply:
                            InputExecution_ms_word(self.reply,self.sentence1)
                        elif "highlight selected text" in self.reply:
                            InputExecution_ms_word(self.reply,self.sentence1)
                        elif "add borders to selection" in self.reply:
                            InputExecution_ms_word(self.reply,self.sentence1)
                        #view self.reply,self.sentence1s    
                        elif "switch to print layout view" in self.reply:
                            InputExecution_ms_word(self.reply,self.sentence1)
                        elif "switch to read mode" in self.reply:
                            InputExecution_ms_word(self.reply,self.sentence1)
                        elif "switch to web layout view" in self.reply:
                            InputExecution_ms_word(self.reply,self.sentence1)
                        elif "switch to outline view" in self.reply:
                            InputExecution_ms_word(self.reply,self.sentence1)
                        elif "switch to draft view" in self.reply:
                            InputExecution_ms_word(self.reply,self.sentence1)
                        elif "go to the design tab" in self.reply:
                            InputExecution_ms_word(self.reply,self.sentence1)
                        # Design Tab Options
                        elif "change page color" in self.reply:
                            InputExecution_ms_word(self.reply,self.sentence1)
                        elif "apply page borders" in self.reply:
                            InputExecution_ms_word(self.reply,self.sentence1)
                        
                        elif "change theme" in self.reply:
                            InputExecution_ms_word(self.reply,self.sentence1)
                        elif "go to the insert tab" in self.reply:
                            InputExecution_ms_word(self.reply,self.sentence1)
                        # Insert Header
                        elif "insert header" in self.reply:
                            InputExecution_ms_word(self.reply,self.sentence1)
                        # Insert Footer
                        elif "insert footer" in self.reply:
                            InputExecution_ms_word(self.reply,self.sentence1)   
                        # Format Header
                        elif "format header" in self.reply:
                            InputExecution_ms_word(self.reply,self.sentence1)
                        # Format Footer
                        elif "format footer" in self.reply:
                            InputExecution_ms_word(self.reply,self.sentence1)       
                        elif "close document" in self.reply:
                            InputExecution_ms_word(self.reply,self.sentence1)
                        elif "new document" in self.reply:
                            InputExecution_ms_word(self.reply,self.sentence1)
                        elif "save file" in self.reply:
                            InputExecution_ms_word(self.reply,self.sentence1) 
                        #powerpoint
                        elif "powerpoint" in self.reply:
                            InputExecution_ms_ppt(self.reply,self.sentence1)
                        elif "new presentation" in self.reply:
                            InputExecution_ms_ppt(self.reply,self.sentence1)
                        elif "add slide" in self.reply:
                            InputExecution_ms_ppt(self.reply,self.sentence1)   
                        elif "slideshow" in self.reply:
                            InputExecution_ms_ppt(self.reply,self.sentence1) 
                        elif "next slide" in self.reply:
                            InputExecution_ms_ppt(self.reply,self.sentence1) 
                        elif "previous slide" in self.reply:
                            InputExecution_ms_ppt(self.reply,self.sentence1) 
                        elif "stop slideshow" in self.reply:
                            pyautogui.hotkey("esc")
                        elif "insert text" in self.reply:
                            InputExecution_ms_ppt(self.reply,self.sentence1)
                        elif "increase font size" in self.reply:
                            InputExecution_ms_ppt(self.reply,self.sentence1) 
                        elif "bold text" in self.reply:
                            InputExecution_ms_ppt(self.reply,self.sentence1)
                        elif "italicize this" in self.reply:
                            InputExecution_ms_ppt(self.reply,self.sentence1)
                        elif "underline the selected text" in self.reply:
                            InputExecution_ms_ppt(self.reply,self.sentence1)   
                        elif "align left" in self.reply:
                            InputExecution_ms_ppt(self.reply,self.sentence1)
                        elif "align centre" in self.reply:
                            InputExecution_ms_ppt(self.reply,self.sentence1)
                        elif "align right" in self.reply:
                            InputExecution_ms_ppt(self.reply,self.sentence1)
                        elif "justify" in self.reply:
                            InputExecution_ms_ppt(self.reply,self.sentence1)        
                        elif "cut this" in self.reply:
                            InputExecution_ms_ppt(self.reply,self.sentence1)
                        elif "copy the selection" in self.reply:
                            InputExecution_ms_ppt(self.reply,self.sentence1)
                        elif "paste" in self.reply:
                            InputExecution_ms_ppt(self.reply,self.sentence1)
                        elif "undo the last action" in self.reply:
                            InputExecution_ms_ppt(self.reply,self.sentence1)
                        elif "redo" in self.reply:
                            InputExecution_ms_ppt(self.reply,self.sentence1)
                        elif "go to the beginning of the line" in self.reply:
                            InputExecution_ms_ppt(self.reply,self.sentence1)
                        elif "go to the end of the document" in self.reply:
                            InputExecution_ms_ppt(self.reply,self.sentence1) 
                        elif "insert image" in self.reply:
                            InputExecution_ms_ppt(self.reply,self.sentence1) 
                        elif "resize image" in self.reply:
                            InputExecution_ms_ppt(self.reply,self.sentence1)
                        elif "align image" in self.reply:
                            InputExecution_ms_ppt(self.reply,self.sentence1) 
                        elif "insert table" in self.reply:
                            InputExecution_ms_ppt(self.reply,self.sentence1)
                        elif "insert down arrow" in self.reply:
                            InputExecution_ms_ppt(self.reply,self.sentence1)
                        elif "insert up arrow" in self.reply:
                            InputExecution_ms_ppt(self.reply,self.sentence1)
                        elif "insert left arrow" in self.reply:
                            InputExecution_ms_ppt(self.reply,self.sentence1)
                        elif "insert right arrow" in self.reply:
                            InputExecution_ms_ppt(self.reply,self.sentence1)
                        elif "insert triangle" in self.reply:
                            InputExecution_ms_ppt(self.reply,self.sentence1)
                        elif "insert oval" in self.reply:
                            InputExecution_ms_ppt(self.reply,self.sentence1)
                        elif "insert rectangle" in self.reply:
                            InputExecution_ms_ppt(self.reply,self.sentence1)
                        elif "insert line" in self.reply:
                            InputExecution_ms_ppt(self.reply,self.sentence1)
                        elif "insert bulletin point" in self.reply:
                            InputExecution_ms_ppt(self.reply,self.sentence1)
                        elif "insert textbox" in self.reply:
                            InputExecution_ms_ppt(self.reply,self.sentence1)
                        elif "insert audio" in self.reply:
                            InputExecution_ms_ppt(self.reply,self.sentence1)
                        elif "insert video" in self.reply:
                            InputExecution_ms_ppt(self.reply,self.sentence1)
                        elif "save file" in self.reply:
                            InputExecution_ms_ppt(self.reply,self.sentence1) 
                        else:
                            speak(self.reply)
            


startExecution=MainThread()

class Main(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui=Ui_enablemateUi()
        self.ui.setupUi(self)
        self.ui.movie=QtGui.QMovie("../G.U.I Material/ExtraGui/initial.gif") 
        self.ui.label_5.setMovie(self.ui.movie)  
        self.ui.movie.start()  
        self.ui.movie=QtGui.QMovie("../G.U.I Material/VoiceReg/Ntuks.gif")  
        self.ui.label_2.setMovie(self.ui.movie)  
        self.ui.movie.start()  
        self.ui.movie=QtGui.QMovie("../G.U.I Material/ExtraGui/Earth.gif")  
        self.ui.label_6.setMovie(self.ui.movie)   
        self.ui.movie.start()   
        self.ui.movie=QtGui.QMovie("../G.U.I Material/ExtraGui/B.G_Template_1.gif")  
        self.ui.label_3.setMovie(self.ui.movie)   
        self.ui.movie.start()   
        startExecution.start()
        
recognizer = cv2.face.LBPHFaceRecognizer_create()   
recognizer.read('trainer/trainer.yml')
cascadePath="cv2\\data\\haarcascade_frontalface_default.xml" # Add your cv2 path
faceCascade=cv2.CascadeClassifier(cascadePath)

font=cv2.FONT_HERSHEY_SIMPLEX
id=2

names=['','Your Name'] #Add your name
cam=cv2.VideoCapture(0,cv2.CAP_DSHOW)
cam.set(3,640)
cam.set(4, 480)
minW=0.1*cam.get(3)
minH=0.1*cam.get(4)

while True:
    ret, img = cam.read()
    converted_image = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    faces=faceCascade.detectMultiScale(converted_image,scaleFactor=1.2,minNeighbors=5,minSize=(int(minW),int(minH)),)

    for (x,y,w,h) in faces:
        cv2.rectangle(img,(x,y),(x+w,y+h),(0,255,0),2)
        id,accuracy=recognizer.predict(converted_image[y:y+h,x:x+w])
        if(accuracy<100):
            id=names[id]
            accuracy="  {0}%".format(round(100-accuracy))
            app=QApplication(sys.argv)
            enable=Main()
            enable.show()

            exit(app.exec_())
        else:
            id="unknown"
            accuracy=" {0}%".format(round(100-accuracy))
        cv2.putText(img,str(id),(x+5,y-5),font,1,(255,255,255),2)
        cv2.putText(img,str(accuracy),(x+5,y+h-5),font,1,(255,255,0),1)

    cv2.imshow('camera',img)
    k=cv2.waitKey(10) & 0xff
    if k==27:
        break
print("Thanks for using") 
cam.release()
cv2.destroyAllWindows()