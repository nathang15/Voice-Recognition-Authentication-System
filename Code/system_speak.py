import pyttsx3

def speak(text):
    newVoiceRate = 150
    engine = pyttsx3.init()
    voices = engine.getProperty('voices')
    engine.setProperty('voice', voices[1].id)
    engine.setProperty('rate',newVoiceRate)
    engine.say(text)
    engine.runAndWait()