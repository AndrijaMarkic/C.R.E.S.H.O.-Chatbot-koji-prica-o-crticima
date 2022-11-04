import time
from stt_tts.stt import speech_to_text
from stt_tts.tts import male_voice
from kivy.app import App
from kivy.uix.gridlayout import GridLayout
from kivy.uix.image import Image
from kivy.uix.button import Button
from kivy.uix.textinput import TextInput
from kivy.core.window import Window
Window.size = (900, 600)

class CRESHO(App):
    def build(self):
        self.window = GridLayout()
        self.icon = 'Logo.ico'

        self.img = Image(source='IMAGE LOGO.png', pos=(200, 5), height=90, width=500)
        self.window.add_widget(self.img)

        self.chat = TextInput(pos=(150, 200), height=400, width=600)
        self.chat.readonly = True
        self.window.add_widget(self.chat)

        self.button = Button(text='SEND', pos=(150,100), background_color='blue',color='red', height=100, width=200, font_name='Calibri', font_size=25)
        self.window.add_widget(self.button)

        self.user = TextInput(pos=(350, 100), height=100, width=400)
        self.window.add_widget(self.user)

        

        return self.window
    
    def intro(self, obj):
        self.chat.text = '''Hello, I am CRESHO. Chatbot who knows almost everything about almost every cartoon or anime. Also I know something about croatian dub of that cartoon. 
Just ask me something:'''
        male_voice('''Hello, I am CRESHO. Chatbot who knows almost everything about almost every cartoon or anime. Also I know something about croatian dub of that cartoon. 
Just ask me something:''')
        time.sleep(13)
        self.chat.text = 'Do want to use speech option? Enter "yes" or "no".'
        

if __name__ == "__main__":
    CRESHO().run()