from stt_tts.tts import male_voice, female_voice
import time
from stt_tts.stt import speech_to_text
from python_data_scripts.conan_data import start_chat_conan
from python_data_scripts.mlp_data import start_chat_mlp
from python_data_scripts.thundercats_2011_data import start_chat_thundercats
from python_data_scripts.spuzvabob_data import start_chat_spongebob
from python_data_scripts.pokemon_data import start_chat_pokemon
from python_data_scripts.conan_chatbot import chat_conan
from python_data_scripts.thundercats_2011_chatbot import chat_thundercats
from python_data_scripts.mlp_chatbot import chat_mlp

con = 0
con2 = 0
option = ''
text_for_intro = ' Enter any subject from this cartoon.\n You can Enter "dub" to hear somethnig about croatian dub of this cartoon.\n Enter "exit" to back to the main menu\n '

while option != 'quit' and option != 'exit':

    if con == 0:
        print('''\n\nHello, I am CRESHO. Chatbot who knows almost everything about almost every cartoon or anime. Also I know something about croatian dub of that cartoon. 
Just ask me something:''')
        male_voice('''Hello, I am cresho. Chatbot who knows almost everything about almost every cartoon or anime. Also i know something about croatian dub of that cartoon.
        Just ask me something:''')
        con = 1
        time.sleep(13)
    
    print('''\n Options: 
 1. Conan the Adventure
 2. My Little Pony: Friendship is Magic
 3. Thundercats (2011)
 4. Pokemon S01 
 5. SpongeBob\n\n Enter any number from the list to begin. 
 Enter "exit" or "quit" to turn off CRESHO.\n''')
    if con2 == 0:
        control = input('\n Do want to use speech option? Enter "yes" or "no".\n ')
        if control.lower() == 'yes':
            con2 = 1
        elif control.lower() == 'no':
            con2 = 2
    
    if con2 == 1:
        option = speech_to_text()
    elif con2 == 2:
        option = input()

    if option.lower() == 'conan' or option.lower() == '1':  
        print('\n You have choice Conan the Adventurer. What you want to know about this show?\n ')
        male_voice('You have choice Conan the Adventurer. What you want to know about this show?')
        print(text_for_intro)
        chat_conan()
        #start_chat_conan()

    elif option.lower() == 'mlp' or option.lower() == 'my little pony' or option.lower() == '2':   
        print('\n You have choice My Little Pony: Friendship is Magic. What you want to know about this show?\n ')
        female_voice('You have choice My Little Pony: Friendship is Magic. What you want to know about this show?')
        print(text_for_intro)
        chat_mlp()
        #start_chat_mlp()
    
    elif option.lower() == 'thundercats' or option.lower() == '3':  
        print('\n You have choice Thundercats (2011). What you want to know about this show?\n ')
        male_voice('You have choice Thundercats (2011). What you want to know about this show?')
        print(text_for_intro)
        chat_thundercats()
        #start_chat_thundercats()
    
    elif option.lower() == 'pokemon' or option.lower() == '4':  
        print('\n You have choice Pokemon S01. What you want to know about this show?\n ')
        male_voice('You have choice Pokemon Season 1. What you want to know about this show?')
        print(text_for_intro)
        start_chat_pokemon()

    elif option.lower() == 'spongebob' or option.lower() == '5':  
        print('\n You have choice SpongeBob SquarePants. What you want to know about this show?\n ')
        female_voice('You have choice SpongeBob SquarePants. What you want to know about this show?')
        print(text_for_intro)
        start_chat_spongebob()

    elif option.lower() == 'quit' or option.lower() == 'exit':
        print("\n Thanks for useing myself.\n")
        male_voice("Thanks for useing myself")
        time.sleep(3)

    else: 
        print("\n Sorry I don't have that option.\n")
        male_voice("Sorry I don't have that option.")