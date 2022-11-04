import sys
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *
from stt_tts.tts import male_voice, hrvatski_voice, female_voice
import time
from python_data_scripts.conan_chatbot import chat_conan
from python_data_scripts.conan_dub_chatbot import chat_conan_dub
from python_data_scripts.mlp_chatbot import chat_mlp
from python_data_scripts.mlp_dub1_chatbot import chat_mlp_dub1
from python_data_scripts.thundercats_2011_chatbot import chat_thundercats
import winsound

text_for_intro = ' Enter any subject from this cartoon.\n You can Enter "dub" to hear somethnig about croatian dub of this cartoon.\n Enter "exit" to back to the main menu\n '

class App(QMainWindow):

    def __init__(self):
        super().__init__()
        self.title = 'C.R.E.S.H.O.'
        self.left = 400
        self.top = 100
        self.width = 1280
        self.height = 720
        self.initUI()
    
    def initUI(self):
        self.con1 = 0
        self.con2 = 0
        self.con3 = 0
        self.con4 = 0
        self.setWindowTitle(self.title)
        self.setGeometry(self.left, self.top, self.width, self.height)
        self.setStyleSheet("background-color: black;")
        self.setWindowIcon(QIcon('Logo.ico'))
    
        self.textbox1 = QTextEdit(self)
        self.textbox1.move(300, 10)
        self.textbox1.resize(680, 400)
        self.textbox1.setStyleSheet("background-color: white;")
        self.textbox1.setFont(QFont('Arian', 12))
        self.textbox1.setReadOnly(True)

        self.textbox2 = QLineEdit(self)
        self.textbox2.move(450, 420)
        self.textbox2.resize(530, 100)
        self.textbox2.setStyleSheet("background-color: white;")
        self.textbox2.setFont(QFont('Arian', 12))
        
        self.button = QPushButton('Send', self)
        self.button.move(300, 420)
        self.button.resize(150, 100)
        self.button.setStyleSheet("QPushButton" "{" "background-color : blue;" "}"
                                  "QPushButton::pressed" "{" "background-color : light blue;" "}")
        self.button.setFont(QFont('Lemon', 15))

        self.button.clicked.connect(self.on_click)

        self.show()

        if self.con3 == 0:
            self.textbox1.insertPlainText(''' Hello, I am CRESHO. Chatbot who knows almost everything about almost every cartoon or anime. Also I know something about croatian dub of that cartoon. 
Just ask me something:''')
            male_voice('''Hello, I am CRESHO. Chatbot who knows almost everything about almost every cartoon or anime. Also I know something about croatian dub of that cartoon. 
Just ask me something:''')
            time.sleep(13)
            self.show()
            self.con3 = 1

        if self.con1 == 0:
            self.textbox1.insertPlainText('''\n Options: 
 1. Conan the Adventure
 2. My Little Pony: Friendship is Magic
 3. Thundercats (2011)\n\n Enter any number from the list to begin. 
 Enter "exit" or "quit" to turn off CRESHO.\n''')
            self.show()
            self.con1 = 1

    @pyqtSlot()
    def on_click(self):
        textboxValue = self.textbox2.text()
        if (textboxValue.lower() == '1' and self.con2 == 0):
            textboxValue = ''
            self.textbox2.clear()
            self.textbox1.clear()
            self.textbox1.insertPlainText(' You have choice Conan the Adventurer. What you want to know about this show?\n ')
            male_voice('You have choice Conan the Adventurer. What you want to know about this show?')
            self.show()
            self.con2 = 1

        elif (textboxValue.lower() == '2' and self.con2 == 0):
            textboxValue = ''
            self.textbox2.clear()
            self.textbox1.clear()
            self.textbox1.insertPlainText(' You have choice My Little Pony: Friendship is Magic. What you want to know about this show?\n ')
            female_voice('You have choice My Little Pony: Friendship is Magic. What you want to know about this show?')
            self.show()
            self.con2 = 2
        
        elif (textboxValue.lower() == '3' and self.con2 == 0):
            textboxValue = ''
            self.textbox2.clear()
            self.textbox1.clear()
            self.textbox1.insertPlainText(' You have choice Thundercats (2011). What you want to know about this show?\n ')
            male_voice('You have choice Thundercats (2011). What you want to know about this show?')
            self.show()
            self.con2 = 3
        
        elif ((textboxValue.lower() == 'exit' or textboxValue.lower() == 'quit') and (self.con2 == 0 and self.con4 == 0)):
            textboxValue = ''
            self.textbox2.clear()
            self.textbox1.clear()
            self.textbox1.insertPlainText(' Thanks for useing myself.\n ')
            male_voice('Thanks for useing myself.')
            self.show()
            time.sleep(5)
            self.show()
            self.close()

        elif ((self.con2 == 0 and self.con4 == 0) and (textboxValue != '1' or textboxValue != '2' or textboxValue != '3' or textboxValue != 'exit' or textboxValue != 'quit')):
            textboxValue = ''
            self.textbox2.clear()
            male_voice('Sorry I dont have that option.')
            self.show()
            
        if ((self.con2 == 1 or self.con2 == 2 or self.con2 == 3)  and textboxValue != ''): 
            if ((textboxValue.lower() == 'exit' or textboxValue.lower() == 'quit') and ((self.con2 == 1 or self.con2 == 2 or self.con2 == 3) and self.con4 == 0)):
                winsound.PlaySound(None, winsound.SND_PURGE)
                self.textbox1.insertPlainText('\n CRESHO: back to the main menu\n ')
                male_voice('Back to the main menu')
                self.textbox2.clear()
                self.show()
                self.textbox1.clear()
                self.con2 = 0
                self.textbox1.insertPlainText('''\n Options: 
 1. Conan the Adventure
 2. My Little Pony: Friendship is Magic
 3. Thundercats (2011)\n\n Enter any number from the list to begin. 
 Enter "exit" or "quit" to turn off CRESHO.\n''')
                self.show()

            elif (textboxValue.lower() == 'intro' and self.con2 == 1 and self.con4 == 0):
                winsound.PlaySound(None, winsound.SND_PURGE)
                textboxValue = ''
                self.textbox2.clear()
                self.textbox1.insertPlainText('\n CRESHO: Playing Conan Theme Song from youtube.com\n ')
                male_voice('playing Conan Theme Song from Youtube dot com')
                self.show()
                time.sleep(5)
                winsound.PlaySound('intros/conan_intro.wav', winsound.SND_ASYNC)

            elif (textboxValue.lower() == 'stop' and self.con2 == 1 and self.con4 == 0):
                winsound.PlaySound(None, winsound.SND_PURGE)
                self.textbox2.clear()
                self.textbox1.insertPlainText('')
                self.show()

            elif (textboxValue.lower() == 'dub' and self.con2 == 1 and self.con4 == 0):
                textboxValue = ''
                self.textbox2.clear()
                self.textbox1.clear()
                self.textbox1.insertPlainText(' Odabrali ste Conan Pustolov HR Sinkronizacija. Što želite znati o sinkronizaciji?\n ')
                hrvatski_voice('Odabrali ste Conan Pustolov hrvatska Sinkronizacija. Što želite znati o sinkronizaciji?')
                self.show()
                self.con4 = 1

            elif ((textboxValue.lower() == 'exit' or textboxValue.lower() == 'quit') and (self.con4 == 1 and self.con2 == 1)):
                winsound.PlaySound(None, winsound.SND_PURGE)
                self.textbox1.insertPlainText('\n CRESHO: back to the Conan Category.\n ')
                male_voice('Back to the Conan Category.')
                self.textbox2.clear()
                self.show()
                self.textbox1.clear()
                self.con4 = 0

            elif (textboxValue.lower() == 'stop' and self.con4 == 1 and self.con2 == 1):
                winsound.PlaySound(None, winsound.SND_PURGE)
                self.textbox2.clear()
                self.textbox1.insertPlainText('')
                self.show()

            elif (textboxValue.lower() == 'intro' and self.con4 == 1 and self.con2 == 1):
                winsound.PlaySound(None, winsound.SND_PURGE)
                textboxValue = ''
                self.textbox2.clear()
                self.textbox1.insertPlainText('\n CRESHO: Puštam Conan Uvodnu Špicu sa Youtube.com\n ')
                hrvatski_voice('Puštam Conan Uvodnu špicu sa jutjuba')
                self.show()
                time.sleep(5)
                winsound.PlaySound('intros/conan_intro_dub.wav', winsound.SND_ASYNC)

            elif ((self.con4 == 1 and self.con2 == 1) and (textboxValue != 'intro' and textboxValue != 'stop')):
                self.textbox1.insertPlainText(f'\n User: {textboxValue} \n')
                self.textbox1.insertPlainText(f'\n CRESHO: {chat_conan_dub(textboxValue)} \n')
                self.textbox2.clear()
                self.show()

            elif ((self.con2 == 1 and self.con4 == 0) and (textboxValue != 'intro' and textboxValue != 'stop')):
                self.textbox1.insertPlainText(f'\n User: {textboxValue} \n')
                self.textbox1.insertPlainText(f'\n CRESHO: {chat_conan(textboxValue)} \n')
                self.textbox2.clear()
                self.show()

            elif (textboxValue.lower() == 'intro' and self.con2 == 2 and self.con4 == 0):
                winsound.PlaySound(None, winsound.SND_PURGE)
                textboxValue = ''
                self.textbox2.clear()
                self.textbox1.insertPlainText('\n CRESHO: Playing My Little Pony G04 Theme Song from youtube.com\n ')
                female_voice('playing Conan Theme Song from Youtube dot com')
                self.show()
                time.sleep(5)
                winsound.PlaySound('intros/mlp_g04_intro.wav', winsound.SND_ASYNC)

            elif (textboxValue.lower() == 'stop' and self.con2 == 2 and self.con4 == 0):
                winsound.PlaySound(None, winsound.SND_PURGE)
                self.textbox2.clear()
                self.textbox1.insertPlainText('')
                self.show()

            elif (textboxValue.lower() == 'dub' and self.con2 == 2 and self.con4 == 0):
                textboxValue = ''
                self.textbox2.clear()
                self.textbox1.clear()
                self.textbox1.insertPlainText(' Odabrali ste Moj Mali Poni HR Sinkronizacija. Što želite znati o sinkronizaciji?\n ')
                hrvatski_voice('Odabrali ste Moj Mali Poni hrvatska Sinkronizacija. Što želite znati o sinkronizaciji?')
                self.show()
                self.con4 = 2

            elif ((textboxValue.lower() == 'exit' or textboxValue.lower() == 'quit') and (self.con4 == 2 and self.con2 == 2)):
                winsound.PlaySound(None, winsound.SND_PURGE)
                self.textbox1.insertPlainText('\n CRESHO: back to the My Little Pony Category.\n ')
                female_voice('Back to the My Little Pony Category.')
                self.textbox2.clear()
                self.show()
                self.textbox1.clear()
                self.con4 = 0

            elif (textboxValue.lower() == 'stop' and self.con4 == 2 and self.con2 == 2):
                winsound.PlaySound(None, winsound.SND_PURGE)
                self.textbox2.clear()
                self.textbox1.insertPlainText('')
                self.show()

            elif (textboxValue.lower() == 'intro' and self.con4 == 2 and self.con2 == 2):
                winsound.PlaySound(None, winsound.SND_PURGE)
                textboxValue = ''
                self.textbox2.clear()
                self.textbox1.insertPlainText('\n CRESHO: Puštam Moj Mali Poni Uvodnu Špicu sa Youtube.com\n ')
                hrvatski_voice('Puštam Moj Mali Poni Uvodnu špicu sa jutjuba')
                self.show()
                time.sleep(5)
                winsound.PlaySound('intros/mlp_g04_intro_dub1.wav', winsound.SND_ASYNC)

            elif ((self.con4 == 2 and self.con2 == 2) and (textboxValue != 'intro' and textboxValue != 'stop')):
                self.textbox1.insertPlainText(f'\n User: {textboxValue} \n')
                self.textbox1.insertPlainText(f'\n CRESHO: {chat_mlp_dub1(textboxValue)} \n')
                self.textbox2.clear()
                self.show()

            elif ((self.con2 == 2 and self.con4 == 0) and (textboxValue != 'intro' and textboxValue != 'stop')):
                self.textbox1.insertPlainText(f'\n User: {textboxValue} \n')
                self.textbox1.insertPlainText(f'\n CRESHO: {chat_mlp(textboxValue)} \n')
                self.textbox2.clear()
                self.show()

            elif (textboxValue.lower() == 'intro' and self.con2 == 3 and self.con4 == 0):
                winsound.PlaySound(None, winsound.SND_PURGE)
                textboxValue = ''
                self.textbox2.clear()
                self.textbox1.insertPlainText("\n CRESHO: Sorry but this series dosen't have theme song\n ")
                male_voice("Sorry but this series dosen't have theme song")
                self.show()

            elif (textboxValue.lower() == 'stop' and self.con2 == 3 and self.con4 == 0):
                winsound.PlaySound(None, winsound.SND_PURGE)
                self.textbox2.clear()
                self.textbox1.insertPlainText('')
                self.show()

            elif ((self.con2 == 3 and self.con4 == 0) and (textboxValue != 'intro' and textboxValue != 'stop')):
                self.textbox1.insertPlainText(f'\n User: {textboxValue} \n')
                self.textbox1.insertPlainText(f'\n CRESHO: {chat_thundercats(textboxValue)} \n')
                self.textbox2.clear()
                self.show()

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = App()
    sys.exit(app.exec_())