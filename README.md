# EnableMate-A-Voice-Assistant-for-Desktop-Automation

It can do a lot of cool things, some of them being:

- Greet user
- Tell current time and date
- Launch applications/softwares 
- Open any website
- Tells about weather of any city
- Open location of any place plus tells the distance between your place and queried place
- Tells about any person (via Wikipedia)
- Can do various operations in Microsoft Word and PowerPoint.
- Can search anything on Google 
- Can play any video on YouTube
- Take important note in a text file
- Has a cool Graphical User Interface
- Can Recognize Face
- Can generate Images

## Installation
1. **Fork The Repository**
   - Click the "Fork" button on the top right corner of the repository page.
   
2. **Clone The Repository**
   - Clone the forked repository to your local machine:
     git clone <URL>
     
3. **Install Requirements**
   - Install all the requirements given in **[requirements.txt](https://github.com/Anuurag2318/EnableMate-A-Voice-Assistant-for-Desktop-Automation/EnableMate/requirements.txt)** by running the command `pip install -r requirements.txt`
     
4. **Install nltk libraries**  
   - Install all the nltk libraries by just hitting ``` python download_nltk_data.py ```

5. **Capture Face Samples**
- Open the file ```Samplegenerator.py``` and run the following command in your terminal:
  
  ```bash
  python Samplegenerator.py
  ```
- When prompted, enter a unique numeric ID for the face samples (this ID will be used for identifying the individual).
- Look directly at the camera, and the system will capture and save multiple samples of your face in the samples folder. Ensure the lighting is adequate for better accuracy.

6. **Train the Face Model**
- Once you have captured your face samples, open the file Model Trainer.py and run the following command:

  ```bash
  python Model Trainer.py
  ```

- The model will begin training using the face samples you just created. This process builds the recognition model based on the captured images and will save the trained model data for future use.

7. **Train the EnableMate Model**

- Open the file ```Train.py``` and run the following command in your terminal:

  ```bash
  python Train.py
  ```

- The training process will start and may take a few moments to complete. During this time, the model will learn based on the provided intent data.
- Once training is complete, the model will be ready to interpret and respond based on the defined intents.

9. **Run the Assistant**
  - Run the main script:

    ```bash
    python enablemate.py
    ```
    
  - Now Enjoy with your own assistant !!!!

## Contributing

Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.

## Author

👤 **Anurag Tiwari**

## Show your support

Please ⭐️ this repository if this project helped you!
