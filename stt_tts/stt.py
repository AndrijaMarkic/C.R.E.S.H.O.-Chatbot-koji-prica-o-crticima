import speech_recognition as sr

def speech_to_text():
    r = sr.Recognizer()
    while True:
        try:
            MyText=''  
            with sr.Microphone() as source2:
                #r.adjust_for_ambient_noise(source2, duration=0.5)
                audio2 = r.listen(source2)
                MyText = r.recognize_google(audio2)
                MyText = MyText.lower()  # type: ignore
 
                print(MyText)
                if MyText != '':
                    break
                #male_voice2(MyText)
             
        except sr.RequestError as e:
            print("Could not request results; {0}".format(e))
         
        except sr.UnknownValueError:
            print("unknown error occured")
    return MyText
