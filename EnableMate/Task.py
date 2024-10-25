import datetime
from Speak import speak
import pyttsx3
import os
import speech_recognition as sr
import pyautogui
import time
import requests
from Listen import Listen
import urllib.parse
from cookies_bing.bingcookie import u_cookie_value 
from os import system, listdir
from bs4 import BeautifulSoup
from keyboard import press_and_release
def Time():
    time_now = datetime.datetime.now()
    hours = int(time_now.strftime("%I"))
    minutes = time_now.strftime("%M")
    am_pm = time_now.strftime("%p").lower()
    time_formatted = f"{hours} hours {minutes} mins {am_pm}"
    
    speak(f"The time is {time_formatted}")
def rememberExecution(tag,command):
    if 'remember that' in tag:
        remExecute(command)
    elif 'what do you remember' in tag:
        remExecute(command)
    elif 'clear remember file' in tag:
        remExecute(command)
import webbrowser
def GoogleMaps(tag,command):
    if 'directions' in tag:
        speak("Tell me the source")
        source = Listen()
        speak("Tell me the destination you want to go")
        destination = Listen()
        webbrowser.open(f"https://www.google.com/maps/dir/{source}/{destination}")
    elif 'locate' in tag:
        loc = command.replace("locate","")
        webbrowser.open(f"https://www.google.com/maps/place/{loc}")  
def Generate_Images(tag,command):  
    if 'generate an image of' in tag:
        generate(command)

def generate(command):
    if 'generate an image of' in command:
        system(f'python -m BingImageCreator --prompt \"{command}\" -U \"{u_cookie_value}\"')   
        return listdir("output")[-4:]
from PIL import Image
current_index = 0



def ShowImages(tag,current_index=None):
    if "show images" in tag:
        image_folder =  r'output'
        image_files = [f for f in os.listdir(image_folder) if f.lower().endswith(('.png', '.jpg', '.jpeg'))]

        if current_index is None or current_index >= len(image_files):
            current_index = 0

        if current_index < len(image_files):
            image_path = os.path.join(image_folder, image_files[current_index])
            image = Image.open(image_path)
            image.show()
            speak("Say 'close' to close the image: ")
            listening = Listen()
            user_command=listening.lower()
            if user_command == 'close':
                pyautogui.hotkey('ctrl', 'w')
                return True, current_index + 1 
            else:
                print("Invalid command. Image will remain open.")
                return True, current_index
        else:
            print("No more images to show.")
            return False, current_index
        
import wikipedia
def wiki(tag):
    if "wikipedia" in tag:
        speak('Searching wikipedia...')
        query = tag.replace("wikipedia", "")
        results = wikipedia.summary(query, sentences = 3)
        speak("According to wikipedia")
        print(results)
        speak(results)
def remExecute(command):
    if 'remember that' in command:
        rememberMessage=command.replace('remember that','')
        speak('you told me to remember that' + rememberMessage)
        remember=open('remember.txt','a')
        remember.write(rememberMessage)
        remember.close()
    elif 'what do you remember' in command:
        remember=open('remember.txt','r')
        speak('you told me to remember'+remember.read())
    elif 'clear remember file' in command:
        file=open('remember.txt','w')
        file.write(f"")
        speak("done sir! everything i remember has been deleted")
def My_loc(tag):
    if 'my location' in tag:   
        ip_adr = requests.get("https://api.ipify.org").text
        url = "https://get.geojs.io/v1/ip/geo/"+ip_adr+".json"
        geo_q = requests.get(url)
        geo_d = geo_q.json()
        state = geo_d['city']
        country = geo_d['country']
        print(f"you are now in {state , country} .")
        speak(f"you are now in {state , country} .")

def temperatureExecution(tag,command):
    if 'temperature in' in tag:
        url = f"https://www.google.com/search?q={command}"
        r = requests.get(url)
        data = BeautifulSoup(r.text, "html.parser")
        temperature = data.find("div", class_ = "BNeawe").text
        print(f"the temperature is {temperature}")
        speak(f"the temperature is {temperature}")


def youtube_auto(tag):
        if 'on youtube' in tag:
            src_1=tag.replace("open", "")
            src_2 = tag.replace("on youtube", "")
            url = "https://www.youtube.com/results?search_query=" + src_2
            webbrowser.open(url)

def Date():
    date=datetime.datetime.now().strftime("%d of %B %Y")
    speak(f"the date is {date}")
def ms_word(command):
    recognizer = sr.Recognizer()
    engine = pyttsx3.init()
    recognizer.energy_threshold = 4000
    if "start word" in command:
         pyautogui.press('win')
         time.sleep(1)
         search_query = "Word"
         pyautogui.write(search_query, interval=0.1)
         time.sleep(2)
         pyautogui.press('enter')
         time.sleep(5) 
    elif "start writing" in command:    
        engine.say("Initializing typing")
        engine.runAndWait()
        with sr.Microphone() as source: 
         while True:
            audio = recognizer.listen(source)
            try:      
                text = recognizer.recognize_google(audio).lower()

                if "stop writing" in text and "start writing" not in text:
                    engine.say("Stopping writing")
                    engine.runAndWait()
                    break
                text += ". "
                pyautogui.typewrite(text)
            except sr.UnknownValueError:
                pass

    elif "close document" in command:
        pyautogui.hotkey("ctrl", "w")
    # Paragraph Formatting Commands
    elif "align left" in command:
        pyautogui.hotkey("ctrl", "l")  # Left-align text
    elif "align centre" in command:
        pyautogui.hotkey("ctrl", "e")  # Center-align text
    elif "align right" in command:
        pyautogui.hotkey("ctrl", "r")  # Right-align text
    elif "justify" in command:
        pyautogui.hotkey("ctrl", "j")  # Justify text
    elif "scroll down" in command:
        pyautogui.scroll(-3)  # Adjust the value as needed
    elif "select the previous word" in command:
        pyautogui.hotkey("ctrl", "left")
        pyautogui.hotkey("ctrl", "shift", "right")
    elif "select the next paragraph" in command:
        pyautogui.hotkey("ctrl", "down")
        pyautogui.hotkey("ctrl", "shift", "up")
    elif "select all text" in command:
        pyautogui.hotkey("ctrl", "a")
    elif "deselect everything" in command:
        pyautogui.click()   
    elif "find" in command:
        pyautogui.hotkey("ctrl", "f")  
    elif "replace" in command:
        pyautogui.hotkey("ctrl", "h")    
    elif "start spell check" in command:
        pyautogui.hotkey("f7") 
    elif "ignore this word" in command:
        pyautogui.hotkey("ctrl", "d")  
    elif "change misspelled to corrected" in command:
        pyautogui.hotkey("alt", "c")  
        pyautogui.typewrite("corrected")  
        pyautogui.press("enter") 

    # Lists and Bullets
    elif "start numbered list" in command:
        pyautogui.hotkey("alt", "h", "n") 
    elif "start bulleted list" in command:
        pyautogui.hotkey("alt", "h", "u")  

    elif "increase font size" in command:
        pyautogui.hotkey("ctrl", ">")    
    elif "bold text" in command:
        pyautogui.hotkey("ctrl", "b")
    elif "italicize this" in command:
        pyautogui.hotkey("ctrl", "i")
    elif "underline the selected text" in command:
        pyautogui.hotkey("ctrl", "u")
    elif "change font to arial" in command:
        pyautogui.hotkey("ctrl", "d")  
        pyautogui.typewrite("Arial")
        pyautogui.press("enter")
    elif "change font to times new roman" in command:
        pyautogui.hotkey("ctrl", "d")  
        pyautogui.typewrite("Times New Roman")
        pyautogui.press("enter")
    elif "change font size to 12" in command:
        pyautogui.hotkey("ctrl", "shift", "p")  
        pyautogui.typewrite("12")
        pyautogui.press("enter")
    elif "change font size to 16" in command:
        pyautogui.hotkey("ctrl", "shift", "p") 
        pyautogui.typewrite("16")
        pyautogui.press("enter")    
   
    elif "cut this" in command:
        pyautogui.hotkey("ctrl", "x")
    elif "copy the selection" in command:
        pyautogui.hotkey("ctrl", "c")
    elif "paste" in command:
        pyautogui.hotkey("ctrl", "v")
    elif "undo the last action" in command:
        pyautogui.hotkey("ctrl", "z")
    elif "redo" in command:
        pyautogui.hotkey("ctrl", "y")
    elif "go to the beginning of the line" in command:
        pyautogui.hotkey("ctrl", "home")
    elif "go to the end of the document" in command:
        pyautogui.hotkey("ctrl", "end")  



    elif "insert a table" in command:
        pyautogui.hotkey("alt", "n", "t")  
    elif "insert a table with rows and columns" in command:
        pyautogui.hotkey("alt", "n", "t")  
        rows = input("How many rows: ")
        columns = input("How many columns: ")
        pyautogui.typewrite(f"{rows}{' ' * 3}{columns}") 


    elif "format the table" in command:
        pyautogui.hotkey("alt", "h", "ft")  
    elif "format the image" in command:
        pyautogui.hotkey("alt", "h", "p")  # Format the image
    elif "change background color to yellow" in command:
        pyautogui.hotkey("alt", "h", "l", "k", "4")  # Change background color to yellow
    elif "highlight selected text" in command:
        pyautogui.hotkey("alt", "h", "l", "k", "5")  # Highlight selected text (adjust as needed)
    elif "add borders to selection" in command:
        pyautogui.hotkey("alt", "h", "b", "s")  # Add borders to the selection (adjust as needed)
    elif "set table borders" in command:
        pyautogui.hotkey("alt", "h", "b")  # Set table borders
    elif "apply table style" in command:
        pyautogui.hotkey("alt", "h", "t")  # Apply table style
    elif "change cell background color" in command:
        pyautogui.hotkey("alt", "h", "sh", "b")  # Change cell background color
    elif "change text color" in command:
        pyautogui.hotkey("alt", "h", "sh", "f")  # Change text color
    elif "adjust column width" in command:
        pyautogui.hotkey("alt", "h", "sh", "w")  # Adjust column width
    elif "adjust row height" in command:
        pyautogui.hotkey("alt", "h", "sh", "h")  # Adjust row height
    elif "merge cells" in command:
        pyautogui.hotkey("alt", "h", "sh", "m")  # Merge cells
    elif "split cells" in command:
        pyautogui.hotkey("alt", "h", "sh", "s")  # Split cells


    #insertion of image      
    elif "insert an image from file" in command:
        # Ask for the image file path via voice command
        pyautogui.hotkey("alt", "n", "p")  # Insert a picture (Alt, N, P)
        pyautogui.typewrite("Please enter the image file path:")
        audio = recognizer.listen(source)
        try:
            image_path = recognizer.recognize_google(audio).lower()
            if os.path.exists(image_path):
                pyautogui.typewrite(image_path)
                pyautogui.press("enter")
            else:
                print("The specified file path does not exist.")
        except sr.UnknownValueError:
            print("Could not understand the word")


    #formatting of image        
    elif "format the image" in command:
        pyautogui.hotkey("alt", "h", "p")  # Format the image
    elif "set image border" in command:
        pyautogui.hotkey("alt", "h", "s")  # Set image border
    elif "change image size" in command:
        pyautogui.hotkey("alt", "h", "si")  # Change image size
    elif "crop the image" in command:
        pyautogui.hotkey("alt", "h", "c")  # Crop the image
    elif "apply image effects" in command:
        pyautogui.hotkey("alt", "h", "fx")  # Apply image effects
    elif "rotate the image" in command:
        pyautogui.hotkey("alt", "h", "o")  # Rotate the image
    elif "change image brightness" in command:
        pyautogui.hotkey("alt", "h", "b")  # Change image brightness
    elif "adjust image contrast" in command:
        pyautogui.hotkey("alt", "h", "co")  # Adjust image contrast
    elif "compress the image" in command:
        pyautogui.hotkey("alt", "h", "p")  # Compress the image
    elif "reset image formatting" in command:
        pyautogui.hotkey("alt", "h", "e")  # Reset image formatting              


#insertion of list,hyperlink and shapes
    elif "create a bulleted list" in command:
        pyautogui.hotkey("ctrl", "shift", "l")  # Create a bulleted list
    elif "add a comment here" in command:
        pyautogui.hotkey("alt", "r", "c")  # Add a comment
    elif "insert a hyperlink" in command:
        pyautogui.hotkey("ctrl", "k")  #   
    elif "insert a rectangle shape" in command:
        pyautogui.hotkey("alt", "n", "sh", "r")  # Insert a rectangle shape
    elif "insert an oval shape" in command:
        pyautogui.hotkey("alt", "n", "sh", "o")  # Insert an oval shape
    elif "insert a triangle shape" in command:
        pyautogui.hotkey("alt", "n", "sh", "t")  # Insert a triangle shape
    elif "insert a star shape" in command:
        pyautogui.hotkey("alt", "n", "sh", "s")  # Insert a star shape
    elif "insert a line shape" in command:
        pyautogui.hotkey("alt", "n", "sh", "l")  # Insert a line shape
    elif "insert a callout shape" in command:
        pyautogui.hotkey("alt", "n", "sh", "c")  # Insert a callout shape
    elif "change background color to yellow" in command:
        pyautogui.hotkey("alt", "h", "l", "k", "4")  # Change background color to yellow
    elif "highlight selected text" in command:
        pyautogui.hotkey("alt", "h", "l", "k", "5")  # Highlight selected text (adjust as needed)
    elif "add borders to selection" in command:
        pyautogui.hotkey("alt", "h", "b", "s")  # Add borders to the selection (adjust as needed)    


    #view commands    
    elif "switch to print layout view" in command:
        pyautogui.hotkey("alt", "w", "p")  # Switch to Print Layout view
    elif "switch to read mode" in command:
        pyautogui.hotkey("alt", "w", "r")  # Switch to Read Mode
    elif "switch to web layout view" in command:
        pyautogui.hotkey("alt", "w", "l")  # Switch to Web Layout view
    elif "switch to outline view" in command:
        pyautogui.hotkey("alt", "w", "n")  # Switch to Outline view
    elif "switch to draft view" in command:
        pyautogui.hotkey("alt", "w", "d")  # Switch to Draft view
    elif "go to the design tab" in command:
        pyautogui.hotkey("alt", "g", "c")  # Navigate to the Design Tab

    # Design Tab Options
    elif "change page color" in command:
        pyautogui.hotkey("alt", "j")  # Open Page Color menu
        pyautogui.hotkey("alt", "j", "p")  # Select Page Color option

    elif "apply page borders" in command:
        pyautogui.hotkey("alt", "j")  # Open Page Color menu
        pyautogui.hotkey("alt", "j", "b")  # Select Page Borders option

    elif "add watermark" in command:
        pyautogui.hotkey("alt", "j")  # Open Page Color menu
        pyautogui.hotkey("alt", "j", "w")  # Select Watermark option

    elif "change theme" in command:
        pyautogui.hotkey("alt", "j")  # Open Page Color menu
        pyautogui.hotkey("alt", "j", "t")  # Select Themes option 

    elif "go to the insert tab" in command:
        pyautogui.hotkey("alt", "n")  # Navigate to the Insert Tab

    # Insert Header
    elif "insert header" in command:
        pyautogui.hotkey("alt", "n", "h")  # Insert a header

    # Insert Footer
    elif "insert footer" in command:
        pyautogui.hotkey("alt", "n", "f")  # Insert a footer   

    
    # Format Header
    elif "format header" in command:
        pyautogui.hotkey("alt", "p")  # Navigate to the Header & Footer Tools
        pyautogui.hotkey("alt", "h", "o")  # Format header

    # Format Footer
    elif "format footer" in command:
        pyautogui.hotkey("alt", "p")  # Navigate to the Header & Footer Tools
        pyautogui.hotkey("alt", "f", "o")  # Format footer       
    elif "close word" in command:
        pyautogui.hotkey("alt", "f4")  # Close Word                 
#for opening,closing and making of new document
    elif "save document" in command:
        pyautogui.hotkey("ctrl", "s")
    elif "close document" in command:
        pyautogui.hotkey("ctrl", "w")
    elif "open document" in command:
        pyautogui.hotkey("ctrl", "o")        
    elif "new document" in command:
        pyautogui.hotkey("ctrl", "n")
         # Wait for the "New Document" dialog to appear (you can adjust the duration)
        pyautogui.sleep(2)
        

        # Select "Blank document" by simulating keyboard navigation (you may need to adjust the keys)
        pyautogui.press('right')  # Navigate down to "Blank document"
        pyautogui.press('enter')  # Select "Blank document"
    elif "save file" in command:
        pyautogui.hotkey("ctrl","s")
        time.sleep(1)
        engine.say("Please say name of file.")
        engine.runAndWait()
        with sr.Microphone() as source:
            audio = recognizer.listen(source)
            text_to_insert = recognizer.recognize_google(audio)
            pyautogui.write(text_to_insert, interval=0.1)
            pyautogui.press("enter")
            engine.say("File saved.")
            engine.runAndWait()  
# import speedtest
# def speed():
#     st=speedtest.Speedtest()
#     dl=st.download()
#     up=st.upload()
#     speak(f"Speed test is {dl} bit per second downloading speed and {up} bit per second uploading speed")

engine = pyttsx3.init()
recognizer = sr.Recognizer()
def insert_table():
    # Simulate pressing the Alt+N keys
    pyautogui.hotkey('alt', 'n')
    time.sleep(1)  # Increase delay if necessary

    # Simulate pressing the T key
    pyautogui.hotkey('t')
    time.sleep(1)  # Increase delay if necessary

    # Simulate pressing the I key
    pyautogui.hotkey('i')
    time.sleep(1)  # Increase delay if necessary

    # Select the current value and replace it with the new one
    pyautogui.hotkey('ctrl', 'a')
    engine.say("Please specify the number of columns.")
    engine.runAndWait()

    with sr.Microphone() as source:
        audio = recognizer.listen(source)
        try:
            new_columns = recognizer.recognize_google(audio)
            print(f"Recognized columns: {new_columns}")
            pyautogui.write(new_columns, interval=0.1)
        except sr.UnknownValueError:
            engine.say("I didn't catch the number of columns. Please repeat.")
            engine.runAndWait()
            return
        except sr.RequestError:
            print("Could not request results; check your network connection")
            return

    # Move to the next input field and input the number of rows
    pyautogui.hotkey('tab')
    time.sleep(1)  # Increase delay if necessary
    engine.say("Please specify the number of rows.")
    engine.runAndWait()

    with sr.Microphone() as source:
        audio = recognizer.listen(source)
        try:
            new_rows = recognizer.recognize_google(audio)
            print(f"Recognized rows: {new_rows}")
            pyautogui.write(new_rows, interval=0.1)
            pyautogui.press("enter")
        except sr.UnknownValueError:
            engine.say("I didn't catch the number of rows. Please repeat.")
            engine.runAndWait()
            return
        except sr.RequestError:
            print("Could not request results; check your network connection")
            return

    engine.say("Table inserted.")
    engine.runAndWait()

def align_image_left():
    pyautogui.hotkey('alt')
    pyautogui.press('down')
    pyautogui.press('tab', presses=16, interval=0.1)
    pyautogui.press("enter")
    pyautogui.press("enter")

def align_image_right():
    pyautogui.hotkey('alt')
    pyautogui.press('down')
    pyautogui.press('tab', presses=16, interval=0.1)
    pyautogui.press("enter")
    pyautogui.press("down",presses=1,interval=0.1)
    pyautogui.press("enter")

def align_image_center():
    pyautogui.hotkey('alt')
    pyautogui.press('down')
    pyautogui.press('tab', presses=16, interval=0.1)
    pyautogui.press("enter")
    pyautogui.press("down",presses=2,interval=0.1)
    pyautogui.press("enter")

def align_image_top():
    pyautogui.hotkey('alt')
    pyautogui.press('down')
    pyautogui.press('tab', presses=16, interval=0.1)
    pyautogui.press("enter")
    pyautogui.press("down",presses=3,interval=0.1)
    pyautogui.press("enter")

def align_image_middle():
    pyautogui.hotkey('alt')
    pyautogui.press('down')
    pyautogui.press('tab', presses=16, interval=0.1)
    pyautogui.press("enter")
    pyautogui.press("down",presses=4,interval=0.1)
    pyautogui.press("enter")

def align_image_bottom():
    pyautogui.hotkey('alt')
    pyautogui.press('down')
    pyautogui.press('tab', presses=16, interval=0.1)
    pyautogui.press("enter")
    pyautogui.press("down",presses=5,interval=0.1)
    pyautogui.press("enter")

def insert_video():
    # Simulate pressing the Alt+N keys
    pyautogui.hotkey('alt', 'n')
    time.sleep(1)  # Increase delay if necessary

    # Simulate pressing the T key
    pyautogui.hotkey('v')
    time.sleep(1)  # Increase delay if necessary

    # Simulate pressing the I key
    pyautogui.hotkey('enter')
    time.sleep(1)  # Increase delay if necessary

    # Select the current value and replace it with the new one
    engine.say("Select video.")
    engine.runAndWait()   
    time.sleep(10)
    engine.say("video inserted") 

def insert_audio():
    # Simulate pressing the Alt+N keys
    pyautogui.hotkey('alt', 'n')
    time.sleep(1)  # Increase delay if necessary

    # Simulate pressing the T key
    pyautogui.hotkey('o')
    time.sleep(1)  # Increase delay if necessary

    # Simulate pressing the I key
    pyautogui.hotkey('enter')
    time.sleep(1)  # Increase delay if necessary

    # Select the current value and replace it with the new one
    engine.say("Select audio.")
    engine.runAndWait()   
    time.sleep(10)
    engine.say("audio inserted") 

def insert_textbox():
    pyautogui.hotkey('alt', 'n')
    time.sleep(1) 
   
    pyautogui.hotkey('x')
    time.sleep(1)  
    engine.say("Textbox inserted") 
    engine.say("Please say the text to insert.")
    engine.runAndWait()
    with sr.Microphone() as source:
            audio = recognizer.listen(source)
            text_to_insert = recognizer.recognize_google(audio)
            pyautogui.write(text_to_insert, interval=0.1)
            pyautogui.press("enter")
            engine.say("Text inserted.")
            engine.runAndWait()     

    time.sleep(1) 

def insert_table():
    recognizer = sr.Recognizer()
    engine = pyttsx3.init()
    recognizer.energy_threshold = 4000
    # Simulate pressing the Alt+N keys
    pyautogui.hotkey('alt', 'n')
    time.sleep(1)  # Increase delay if necessary

    # Simulate pressing the T key
    pyautogui.hotkey('t')
    time.sleep(1)  # Increase delay if necessary

    # Simulate pressing the I key
    pyautogui.hotkey('i')
    time.sleep(1)  # Increase delay if necessary
    pyautogui.hotkey('ctrl', 'a')
    engine.say("Please specify the number of columns.")
    
    with sr.Microphone() as source:
        audio = recognizer.listen(source)
        try:
            new_columns = recognizer.recognize_google(audio)
            print(f"Recognized columns: {new_columns}")
            pyautogui.write(new_columns, interval=0.1)
        except sr.UnknownValueError:
            engine.say("I didn't catch the number of columns. Please repeat.")
            engine.runAndWait()
    pyautogui.hotkey('tab')
    time.sleep(1)
    engine.say("Please specify the number of rows.")

def ms_ppt(command):
    recognizer = sr.Recognizer()
    engine = pyttsx3.init()
    recognizer.energy_threshold = 4000
    if "open powerpoint" in command:
        # Simulate pressing the Windows key
        pyautogui.press('win')
        time.sleep(1)
        search_query = "Powerpoint"
        pyautogui.write(search_query, interval=0.1)
        time.sleep(2)
        pyautogui.press('enter')
        time.sleep(5)  # Adjust as needed

    elif "new presentation" in command:
        pyautogui.hotkey("ctrl", "n")
        time.sleep(2)

        pyautogui.press('right')
        pyautogui.press('enter')  


    elif "save presentation" in command:
        pyautogui.hotkey("ctrl", "s")
        time.sleep(2) 

    elif "add slide" in command:
        pyautogui.hotkey("ctrl", "m")

    elif "slideshow" in command:
        pyautogui.hotkey("f5")

    elif "finish slideshow" in command:
        pyautogui.hotkey("esc")

    elif "next slide" in command:
        pyautogui.press("right")

    elif "previous slide" in command:
        pyautogui.press("left")

    elif "insert text" in command:
        engine.say("Please say the text to insert.")
        engine.runAndWait()
        with sr.Microphone() as source:
            audio = recognizer.listen(source)
            text_to_insert = recognizer.recognize_google(audio)
            pyautogui.write(text_to_insert, interval=0.1)
            pyautogui.press("enter")
            engine.say("Text inserted.")
            engine.runAndWait()

    elif "insert picture" in command:
        pyautogui.hotkey('alt', 'n')
        time.sleep(2)  # Adjust as needed

        pyautogui.hotkey('z', 'g')
        time.sleep(2)  # Adjust as needed

        pyautogui.hotkey('p')
        time.sleep(2)  # Adjust as needed

        pyautogui.hotkey('d')
        time.sleep(5)  # Adjust as needed
        engine.say("Image inserted.")
        engine.runAndWait()

    elif "resize image" in command:
    
      pyautogui.hotkey('alt')  
      engine.say("Please specify the new height.")
      pyautogui.press('down')
      engine.runAndWait()
      with sr.Microphone() as source:
        audio = recognizer.listen(source)
      try:
         new_height = recognizer.recognize_google(audio)      
         num_tabs = 20
         pyautogui.press('tab', presses=num_tabs, interval=0.1)
         pyautogui.write(new_height, interval=0.1)
         pyautogui.press("enter")
      except sr.UnknownValueError:
        engine.say("I didn't catch the new width. Please repeat.")
        engine.runAndWait()
      time.sleep(1)

      pyautogui.hotkey('alt') 
      engine.say("Please specify the new width.")
      pyautogui.press('down')
      engine.runAndWait()
      with sr.Microphone() as source:
        audio = recognizer.listen(source)
      try:
         new_width = recognizer.recognize_google(audio)      
         num_tabs = 21
         pyautogui.press('tab', presses=num_tabs, interval=0.1)
         pyautogui.write(new_width, interval=0.1)
         pyautogui.press("enter")
      except sr.UnknownValueError:
        engine.say("I didn't catch the new height. Please repeat.")
        engine.runAndWait()
      time.sleep(1)

    elif "save file" in command:
        pyautogui.hotkey("ctrl","s")
        time.sleep(1)
        engine.say("Please say name of file.")
        engine.runAndWait()
        with sr.Microphone() as source:
            audio = recognizer.listen(source)
            text_to_insert = recognizer.recognize_google(audio)
            pyautogui.write(text_to_insert, interval=0.1)
            pyautogui.press("enter")
            engine.say("File saved.")
            engine.runAndWait()     

   
    elif "insert table" in command:
        insert_table() 

    elif "insert video" in command:
        insert_video() 

    elif "insert audio" in command:
        insert_audio()

    elif "insert_textbox"in command:
        insert_textbox()
    
    elif "select all" in command:
        pyautogui.hotkey("ctrl","a")
        time.sleep(0.5)

    elif "insert bulletin point" in command:
     pyautogui.hotkey("alt", "h")
     time.sleep(0.5)
     pyautogui.press("u")
     time.sleep(0.5)
     pyautogui.press("right")
     time.sleep(0.5)
     pyautogui.press("enter")
     engine.say("bulletin point inserted")

    elif "insert line" in command:
     pyautogui.hotkey("alt", "n")
     time.sleep(0.5)

     pyautogui.hotkey("s", "h")
     time.sleep(0.5)

     pyautogui.press("down")
     pyautogui.press("down")  
     pyautogui.press("enter")  

    elif "insert rectangle" in command: 
     pyautogui.hotkey("alt", "n")
     time.sleep(0.5)

     pyautogui.hotkey("s", "h")
     time.sleep(0.5)

     pyautogui.press("down")
     pyautogui.press("down")  
     pyautogui.press("down")
     pyautogui.press("enter")     

    elif "insert oval" in command: 
     pyautogui.hotkey("alt", "n")
     time.sleep(0.5)

     pyautogui.hotkey("s", "h")
     time.sleep(0.5)

     pyautogui.press("down")
     pyautogui.press("down")  
     pyautogui.press("down")
     pyautogui.press("down")
     pyautogui.press("right")
     pyautogui.press("enter")

    elif "insert triangle" in command: 
     pyautogui.hotkey("alt", "n")
     time.sleep(0.5)

     pyautogui.hotkey("s", "h")
     time.sleep(0.5)

     pyautogui.press("down")
     pyautogui.press("down")  
     pyautogui.press("down")
     pyautogui.press("down")
     pyautogui.press("right")
     pyautogui.press("right")
     pyautogui.press("enter")

    elif "insert right arrow" in command: 
     pyautogui.hotkey("alt", "n")
     time.sleep(0.5)

     pyautogui.hotkey("s", "h")
     time.sleep(0.5)
     num_tabs = 8
     pyautogui.press('down', presses=num_tabs, interval=0.1)
     pyautogui.press("enter")

    elif "insert left arrow" in command: 
     pyautogui.hotkey("alt", "n")
     time.sleep(0.5)

     pyautogui.hotkey("s", "h")
     time.sleep(0.5)

     time.sleep(0.5)
     num_tabs = 8
     pyautogui.press('down', presses=num_tabs, interval=0.1)
     pyautogui.press("right")
     pyautogui.press("enter")

    elif "insert up arrow" in command: 
     pyautogui.hotkey("alt", "n")
     time.sleep(0.5)

     pyautogui.hotkey("s", "h")
     time.sleep(0.5)

     time.sleep(0.5)
     num_tabs = 8
     pyautogui.press('down', presses=num_tabs, interval=0.1)
     pyautogui.press("right")
     pyautogui.press("right")
     pyautogui.press("enter")

    elif "insert down arrow" in command: 
     pyautogui.hotkey("alt", "n")
     time.sleep(0.5)

     pyautogui.hotkey("s", "h")
     time.sleep(0.5)

     time.sleep(0.5)
     num_tabs = 8
     pyautogui.press('down', presses=num_tabs, interval=0.1)
     pyautogui.press("right")
     pyautogui.press("right")
     pyautogui.press("right")
     pyautogui.press("enter")     
 
    elif "align image" in command:
        engine.say("Please specify alignment like left, right, center, top, middle, or bottom.")
        engine.runAndWait()

        with sr.Microphone() as source:
            audio = recognizer.listen(source)

        try:
            alignment_option = recognizer.recognize_google(audio).lower()

            switch_dict = {
                'left': align_image_left,
                'right': align_image_right,
                'center': align_image_center,
                'top': align_image_top,
                'middle': align_image_middle,
                'bottom': align_image_bottom
            }

            if alignment_option in switch_dict:
                switch_dict[alignment_option]()
            else:
                engine.say("Invalid alignment option. Please repeat.")
                engine.runAndWait()

        except sr.UnknownValueError:
            engine.say("I didn't catch the alignment option. Please repeat.")
            engine.runAndWait()

        time.sleep(1) 
import speedtest

def convert_speed(speed_in_bytes):
    speed_in_kbps = speed_in_bytes / 1024
    speed_in_mbps = speed_in_kbps / 1024
    return speed_in_mbps

def speed():
    st = speedtest.Speedtest()
    dl_bytes = st.download()
    up_bytes = st.upload()

    dl_mbps= convert_speed(dl_bytes)
    up_mbps= convert_speed(up_bytes)

    speak(f"Downloading speed:{dl_mbps:.2f} Mbps and Uploading speed:{up_mbps:.2f} Mbps")
def NonInputExecution(query):
    query=str(query).lower()
    if "time" in query:
        Time()
    elif "date" in query:
        Date()
    elif "internet speed" in query:
        speed()

def InputExecution_ms_word(tag,command):
    command = str(command)
    if "word" in tag:
        ms_word(command)
    elif "start writing" in tag:
        ms_word(command)
    elif "save document" in tag:
        ms_word(command)
    elif "close document" in tag:
        ms_word(command)
    elif "align left" in tag:
        ms_word(command)
    elif "align centre" in tag:
        ms_word(command)
    elif "align right" in tag:
        ms_word(command)
    elif "justify" in tag:
        ms_word(command)
    elif "scroll down" in tag:
        ms_word(command)
    elif "select the previous word" in tag:
        ms_word(command)
    elif "select the next paragraph" in tag:
        ms_word(command)
    elif "select all text" in tag:
        ms_word(command)
    elif "deselect everything" in tag:
        ms_word(command)  
    elif "find" in tag:
        ms_word(command)
    elif "replace" in tag:
        ms_word(command) 
    elif "start spell check" in tag:
        ms_word(command)
    elif "ignore this word" in tag:
        ms_word(command)
    elif "change misspelled to corrected" in tag:
        ms_word(command)

    elif "start numbered list" in tag:
        ms_word(command)
    elif "start bulleted list" in tag:
        ms_word(command)


    elif "increase font size" in tag:
        ms_word(command) 
    elif "bold text" in tag:
        ms_word(command)
    elif "italicize this" in tag:
        ms_word(command)
    elif "underline the selected text" in tag:
        ms_word(command)
    elif "change font to arial" in tag:
        ms_word(command)
    elif "change font to times new roman" in tag:
        ms_word(command)
    elif "change font size to 12" in tag:
        ms_word(command)
    elif "change font size to 16" in tag:
       ms_word(command)

    elif "cut this" in tag:
        ms_word(command)
    elif "copy the selection" in tag:
        ms_word(command)
    elif "paste" in command:
        ms_word(command)
    elif "undo the last action" in tag:
        ms_word(command)
    elif "redo" in command:
        ms_word(command)
    elif "go to the beginning of the line" in tag:
        ms_word(command)
    elif "go to the end of the document" in tag:
        ms_word(command) 

    elif "insert a table" in tag:
        ms_word(command)
    elif "insert a table with rows and columns" in tag:
        ms_word(command)                      

    elif "format the table" in tag:
        ms_word(command)
    elif "format the image" in tag:
        ms_word(command)
    elif "change background color to yellow" in tag:
        ms_word(command)
    elif "highlight selected text" in tag:
        ms_word(command)
    elif "add borders to selection" in tag:
        ms_word(command)
    elif "set table borders" in tag:
        ms_word(command)
    elif "apply table style" in tag:
        ms_word(command)
    elif "change cell background color" in tag:
        ms_word(command)
    elif "change text color" in tag:
        ms_word(command)
    elif "adjust column width" in tag:
        ms_word(command)
    elif "adjust row height" in tag:
        ms_word(command)
    elif "merge cells" in tag:
        ms_word(command)
    elif "split cells" in tag:
        ms_word(command)

    
    elif "insert an image from file" in tag:
        ms_word(command)
    elif "format the image" in tag:
        ms_word(command)
    elif "set image border" in tag:
        ms_word(command)
    elif "change image size" in tag:
        ms_word(command)
    elif "crop the image" in tag:
        ms_word(command)
    elif "apply image effects" in tag:
        ms_word(command)
    elif "rotate the image" in tag:
        ms_word(command)
    elif "change image brightness" in tag:
        ms_word(command)
    elif "adjust image contrast" in tag:
        ms_word(command)
    elif "compress the image" in tag:
        ms_word(command)
    elif "reset image formatting" in tag:
        ms_word(command)              


    elif "create a bulleted list" in tag:
        ms_word(command)
    elif "add a comment here" in tag:
        ms_word(command)
    elif "insert a hyperlink" in tag:
        ms_word(command)   
    elif "insert a rectangle shape" in tag:
        ms_word(command)
    elif "insert an oval shape" in tag:
        ms_word(command)
    elif "insert a triangle shape" in tag:
        ms_word(command)
    elif "insert a star shape" in tag:
        ms_word(command)
    elif "insert a line shape" in tag:
        ms_word(command)
    elif "insert a callout shape" in tag:
        ms_word(command)
    elif "change background color to yellow" in tag:
        ms_word(command)
    elif "highlight selected text" in tag:
       ms_word(command)
    elif "add borders to selection" in tag:
        ms_word(command)

    elif "switch to print layout view" in tag:
        ms_word(command)
    elif "switch to read mode" in tag:
        ms_word(command)
    elif "switch to web layout view" in tag:
        ms_word(command)
    elif "switch to outline view" in tag:
        ms_word(command)
    elif "switch to draft view" in tag:
        ms_word(command)
    elif "go to the design tab" in tag:
        ms_word(command)

    # Design Tab Options
    elif "change page color" in tag:
        ms_word(command)

    elif "apply page borders" in tag:
        ms_word(command)

    elif "add watermark" in tag:
        ms_word(command)

    elif "change theme" in tag:
        ms_word(command)

    elif "go to the insert tab" in tag:
        ms_word(command)

    # Insert Header
    elif "insert header" in tag:
        ms_word(command)

    # Insert Footer
    elif "insert footer" in tag:
        ms_word(command)   

    
    # Format Header
    elif "format header" in tag:
        ms_word(command)

    # Format Footer
    elif "format footer" in tag:
        ms_word(command)       
    elif "close word" in tag:
        ms_word(command)
    elif "save document" in tag:
        ms_word(command)
    elif "close document" in tag:
        ms_word(command)
    elif "open document" in tag:
        ms_word(command)
    elif "new document" in tag:
        ms_word(command)
    elif "save file" in tag:
        ms_word(command)  


def InputExecution_ms_ppt(tag,command):
     command = str (command)
     if "powerpoint" in tag:
         ms_ppt(command)
     elif "new presentation" in tag:
         ms_ppt(command)
     elif "add slide" in tag:
        ms_ppt(command)    
     elif "insert text" in tag:
        ms_ppt(command)
     elif "increase font size" in tag:
        ms_ppt(command) 
     elif "bold text" in tag:
        ms_ppt(command)
     elif "italicize this" in tag:
        ms_ppt(command)
     elif "underline the selected text" in tag:
        ms_ppt(command)   
     elif "align left" in tag:
        ms_ppt(command)
     elif "align centre" in tag:
        ms_ppt(command)
     elif "align right" in tag:
        ms_ppt(command)
     elif "justify" in tag:
        ms_ppt(command)        
     elif "cut this" in tag:
        ms_ppt(command)
     elif "copy the selection" in tag:
        ms_ppt(command)
     elif "paste" in command:
        ms_ppt(command)
     elif "undo the last action" in tag:
        ms_ppt(command)
     elif "redo" in command:
        ms_ppt(command)
     elif "go to the beginning of the line" in tag:
        ms_ppt(command)
     elif "go to the end of the document" in tag:
        ms_ppt(command) 

     elif "insert image" in tag:
         ms_ppt(command) 
     elif "resize image" in tag:
         ms_ppt(command)
     elif "align image" in tag:
         ms_ppt(command) 
     elif "insert table" in tag:
         ms_ppt(command)    
     elif "insert down arrow" in tag:
         ms_ppt(command)
     elif "insert up arrow" in tag:
         ms_ppt(command)
     elif "insert left arrow" in tag:
         ms_ppt(command)
     elif "insert right arrow" in tag:
         ms_ppt(command)
     elif "insert triangle" in tag:
         ms_ppt(command)
     elif "insert oval" in tag:
         ms_ppt(command)
     elif "insert rectangle" in tag:
         ms_ppt(command)
     elif "insert line" in tag:
         ms_ppt(command)
     elif "insert bulletin point" in tag:
         ms_ppt(command)
     elif "insert textbox"  in tag:
         ms_ppt(command)
     elif "insert audio" in tag:
         ms_ppt(command)
     elif "insert video" in tag:
         ms_ppt(command)
     elif "save file" in tag:
         ms_ppt(command)    
     elif "slideshow" in tag:
         ms_ppt(tag)  
     elif "next slide" in tag:
         ms_ppt(tag)
     elif "previous slide" in tag:
         ms_ppt(tag)
     elif "finish slideshow" in tag:
         ms_ppt(tag)