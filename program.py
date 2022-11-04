from tkinter import *

from click import command
from stt_tts.tts import male_voice
from stt_tts.stt import speech_to_text
import time

root = Tk()

con = 0
con2 = 0
option = ''

root.title("C.R.E.S.H.O.")
root.geometry('900x600')
root.configure(bg='black')
root.iconbitmap(r'Logo.ico')

def textbox_text():
    messageWindow.tag_add('sel', '1.0', END)
    data = messageWindow.selection_get()
    chatWindow.insert(END, data)
    messageWindow.delete('sel.first', 'sel.last')

def callback():
    global buttonClicked
    buttonClicked = not buttonClicked

buttonClicked = False

chatWindow = Text(root, bd=1, bg='white', width=50, height=8, font=('Arial', 12), foreground='black')
chatWindow.place(x=150, y=10, height=400, width=600)

messageWindow = Text(root, bg='white', width=30, height=4, font=('Arial', 12), foreground='black')
messageWindow.place(x=350, y=420, height=100, width=400)

Button = Button(root, text='Send', bg='blue', activebackground='light blue', width=12,height=5, font=('Lemon', 20), command=lambda: textbox_text())
Button.place(x=150, y=420, height=100, width=200, )

#scrollbar = Scrollbar(root, command=chatWindow.yview) 
#scrollbar.place(x=750, y=10, height=400, width=25)

if con == 0:
    chatWindow.insert(END, '''Hello, I am CRESHO. Chatbot who knows almost everything about almost every 
cartoon or anime. Also I know something about croatian dub of that cartoon. 
Just ask me something:''')
    male_voice('''Hello, I am CRESHO. Chatbot who knows almost everything about almost every 
cartoon or anime. Also I know something about croatian dub of that cartoon. 
Just ask me something:''')
    con = 1

if con2 == 0 and con==1:
    chatWindow.insert(INSERT,'\n Do want to use speech option? Enter "yes" or "no".\n ')
    if buttonClicked == True:
        control = 
    print(control)
    if control.lower() == 'yes':
            con2 = 1
    elif control.lower() == 'no':
            con2 = 2

    if con2 == 1:
        chatWindow.insert(INSERT,'''\n Options: 
 1. Conan the Adventure
 2. My Little Pony: Friendship is Magic
 3. Thundercats (2011)
 4. Pokemon S01 
 5. SpongeBob\n\n Enter any number from the list to begin. 
 Enter "exit" or "quit" to turn off CRESHO.\n''')
        option = speech_to_text()
    elif con2 == 2:
        chatWindow.insert(INSERT,'''\n Options: 
 1. Conan the Adventure
 2. My Little Pony: Friendship is Magic
 3. Thundercats (2011)
 4. Pokemon S01 
 5. SpongeBob\n\n Enter any number from the list to begin. 
 Enter "exit" or "quit" to turn off CRESHO.\n''')
        option = textbox_text()

root.mainloop()