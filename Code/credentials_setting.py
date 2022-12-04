import whisper
import sounddevice as sd
from scipy.io.wavfile import write
from hash_salt import *
import re
import yaml
import os
from system_speak import *

#load model
#path = your desired path
model = whisper.load_model("small")
fs = 44100  # Sample rate
seconds = 3  # Duration of recording

#setting username
def username_setup():
    usernameList = []
    speak("Please speak into the microphone your desire username 3 times.")
    speak("Now setting the username")
    for i in range(3):
        speak("This is recording number " + str(i + 1))
        username_record = sd.rec(int(seconds * fs), samplerate=fs, channels=2)
        print("recording...")
        sd.wait()
        print("finished")
        write(path + "username.mp3", fs, username_record)
        result = model.transcribe(path + "username.mp3")
        output = result["text"].lower()
        usernameList.append(re.sub('\W+','', output)) #eliminate special characters and spaces
    return usernameList


#setting password    
def pass_setup():
    passList = []
    speak("Please speak into the microphone your desire passphrase 3 times.")
    speak("Now setting up password")
    for i in range(3):
        speak("This is recording number " + str(i + 1))
        myrecording = sd.rec(int(seconds * fs), samplerate=fs, channels=2)
        print("recording...")
        sd.wait()  # Wait until recording is finished
        print("finished")
        write(path + "audio" + str(i) + ".mp3", fs, myrecording)  # Save as mp3 file  
        result = model.transcribe(path + "audio" + str(i) + ".mp3")
        output = result["text"].lower() 
        passList.append(re.sub('\W+','', output)) #eliminate special characters and spaces
    return passList

#Compare the user's attempts to prompt for retry
def compareElements(list):
    element = list[0]
    check = True
    # Comparing each element with first item
    for item in list:
        if element != item:
            check = False
            break
    if (check == True):
        return check
    else:
        return False

#database to store username and corresponding password
d = {}
def database(username, pwd):
    d[username] = hash_salt(pwd)
    if not os.path.exists(path + 'output.yaml'):
        with open(rpath + 'output.yaml', 'w') as file:
            yaml.dump(d, file)
    else:
        
        with open(rpath + 'output.yaml', 'a') as file:
            yaml.dump(d, file)
    return d
