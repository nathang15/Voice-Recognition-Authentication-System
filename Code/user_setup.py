import whisper
import sounddevice as sd
from scipy.io.wavfile import write
from hash_salt import *
import re
import sys
from credentials_setting import *
from system_speak import *

#load model
path = "D:\\AI-based speech recognition login system\\voice_input_output\\"
model = whisper.load_model("small")
fs = 44100  # Sample rate
seconds = 3  # Duration of recording

#setting up the user for the first time or reset the user
def user_setup():
    speak("Do you want to setup a new user? ")
    recording = sd.rec(int(seconds * fs), samplerate=fs, channels=2)
    sd.wait()
    write(path + "answer.mp3", fs, recording)
    result = model.transcribe(path + "answer.mp3")
    answer = result["text"].lower()
    answer =re.sub("[^A-Z]", "", answer,0,re.IGNORECASE)
    print(answer)
    if(answer == "yes" or answer == "Yes"):
        speak("Please set your username")
        usernameList = username_setup()
        print(usernameList)
        if(compareElements(usernameList) == True):
            speak("Your username has been set")
            speak("Please set up your password")
            passList = pass_setup()
            print(passList)
            if(compareElements(passList) == True):
                speak("Your password has been set")
                database(usernameList[0], passList[0])
                speak("User setup is now completed")
            else:
                speak("System now exiting due to mismatching passphrases.")
                sys.exit()
        else:
            speak("System now exiting due to mismatching usernames.") 
            sys.exit()
    elif(answer == "no" or answer == "No"):
        speak("Have a great day!")
        sys.exit() 
    else:
        speak("Invalid response.")
        sys.exit()