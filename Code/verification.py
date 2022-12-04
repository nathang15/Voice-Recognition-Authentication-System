import whisper
import sounddevice as sd
from scipy.io.wavfile import write
from hash_salt import *
import re
import bcrypt
from credentials_setting import *
from system_speak import *
from user_setup import *

#load model
path = "D:\\AI-based speech recognition login system\\voice_input_output\\"
model = whisper.load_model("small")
fs = 44100  # Sample rate
seconds = 3  # Duration of recording

def verify():
    if not os.path.exists('D:\AI-based speech recognition login system\\Code\\output.yaml'):
        speak("There is no existed user in the database. Please create a user first.")
        user_setup()
    else:
        #username_input
        speak("Please say your username ")
        recording = sd.rec(int(seconds * fs), samplerate=fs, channels=2)
        sd.wait()
        write(path + "username_input.mp3", fs, recording)
        result = model.transcribe(path + "username_input.mp3")
        username = result["text"].lower()
        username =re.sub('\W+','', username)
        print(username)
        #username = input("Please enter your username ")

        #passphrase_input
        speak("Please say your passphrase ")
        recording = sd.rec(int(seconds * fs), samplerate=fs, channels=2)
        sd.wait()
        write(path + "passphrase_input.mp3", fs, recording)
        result = model.transcribe(path + "passphrase_input.mp3")
        pwd = result["text"].lower()
        pwd =re.sub('\W+','', pwd)
        print(pwd)

        with open('D:\AI-based speech recognition login system\\Code\\output.yaml') as file:
            try:
                databaseConfig = yaml.safe_load(file)   
                #print(databaseConfig)
                passwd = pwd.encode()
                if(bcrypt.checkpw(passwd, databaseConfig[username])):
                    print('match')
                    return True
                else:
                    print('no match')
                    return False
            except yaml.YAMLError as exc:
                print(exc)