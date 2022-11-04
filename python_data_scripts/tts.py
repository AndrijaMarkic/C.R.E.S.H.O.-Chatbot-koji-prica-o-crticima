import pyttsx3
import winsound

def male_voice(text):
    male = pyttsx3.init()
    male.setProperty('voice', "HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Speech\Voices\Tokens\Vocalizer Expressive tom premium-high 22kHz")
    male.setProperty('rate', 180)
    male.save_to_file(text, 'text.wav')
    #male.say(text)
    male.runAndWait()
    winsound.PlaySound('text.wav', winsound.SND_ASYNC)

def female_voice(text):
    female = pyttsx3.init()
    female.setProperty('voice', 'HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Speech\Voices\Tokens\Vocalizer Expressive susan premium-high 22kHz')
    female.setProperty('rate', 180)
    female.save_to_file(text, 'text.wav')
    #female.say(text)
    female.runAndWait()
    winsound.PlaySound('text.wav', winsound.SND_ASYNC)

def hrvatski_voice(text):
    hrvatski = pyttsx3.init()
    hrvatski.setProperty('voice', 'HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Speech\Voices\Tokens\MSTTS_V110_hrHR_Matej')
    hrvatski.setProperty('rate', 180)
    hrvatski.setProperty('volume', 100)
    hrvatski.save_to_file(text, 'text.wav')
    #hrvatski.say(text)
    hrvatski.runAndWait()
    winsound.PlaySound('text.wav', winsound.SND_ASYNC)

def male_voice2(text):
    male2 = pyttsx3.init()
    male2.setProperty('voice', "HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Speech\Voices\Tokens\Vocalizer Expressive daniel premium-high 22kHz")
    male2.setProperty('rate', 180)
    male2.setProperty('volume', 75)
    male2.save_to_file(text, 'text.wav')
    #male2.say(text)
    male2.runAndWait()
    winsound.PlaySound('text.wav', winsound.SND_ASYNC)