import pyttsx3
import winsound

def male_voice(text):
    male = pyttsx3.init()
    male.setProperty('voice', "HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Speech\Voices\Tokens\TTS_MS_EN-US_DAVID_11.0")
    male.setProperty('rate', 180)
    male.save_to_file(text, 'text.wav')
    #male.say(text)
    male.runAndWait()
    winsound.PlaySound('text.wav', winsound.SND_ASYNC)

def female_voice(text):
    female = pyttsx3.init()
    female.setProperty('voice', 'HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Speech\Voices\Tokens\TTS_MS_EN-US_ZIRA_11.0')
    female.setProperty('rate', 180)
    female.save_to_file(text, 'text.wav')
    #female.say(text)
    female.runAndWait()
    winsound.PlaySound('text.wav', winsound.SND_ASYNC)

def hrvatski_voice(text):
    hrvatski = pyttsx3.init()
    hrvatski.setProperty('voice', 'HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Speech\Voices\Tokens\MSTTS_V110_hrHR_Matej')
    hrvatski.setProperty('rate', 160)
    hrvatski.setProperty('volume', 100)
    hrvatski.save_to_file(text, 'text.wav')
    #hrvatski.say(text)
    hrvatski.runAndWait()
    winsound.PlaySound('text.wav', winsound.SND_ASYNC)