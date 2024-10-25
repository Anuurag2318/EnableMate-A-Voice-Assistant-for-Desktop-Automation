import cv2
import numpy as np
from PIL import Image
import os
import re 
path = 'samples'
recognition = cv2.face.LBPHFaceRecognizer_create()
detector = cv2.CascadeClassifier("cv2\\data\\haarcascade_frontalface_default.xml") # Add your cv2 path

def Images_And_Labels(path):
    imagePaths = [os.path.join(path, f) for f in os.listdir(path)]
    faceSamples = []
    ids = []
    for imagePath in imagePaths:
        gray_img = Image.open(imagePath).convert('L')
        img_arr = np.array(gray_img, 'uint8')
        faces = detector.detectMultiScale(img_arr)
        
        # Extract the id from the filename using a regular expression
        match = re.search(r'\.(\d+)\.', os.path.basename(imagePath))
        if match:
            id = int(match.group(1))
            for (x, y, w, h) in faces:
                faceSamples.append(img_arr[y:y+h, x:x+w])
                ids.append(id)

    return faceSamples, ids

print("Training faces")
faces, ids = Images_And_Labels(path)
if faces:
    recognition.train(faces, np.array(ids))
    recognition.write('trainer/trainer.yml')
    print('Model trained')
else:
    print('No faces detected for training. Please check your data.')
