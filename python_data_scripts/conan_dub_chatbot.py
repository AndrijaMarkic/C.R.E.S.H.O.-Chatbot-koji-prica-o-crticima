import nltk
from nltk.stem import WordNetLemmatizer
lemmatizer = WordNetLemmatizer()
import pickle
import numpy as np
import json
import random
from keras.models import load_model
from stt_tts.stt import speech_to_text
from stt_tts.tts import male_voice , hrvatski_voice
import time
import winsound

model = load_model('models/conan_dub_chatbot_model.h5')

with open("databases/Conan the Adventurer/conan_dub.json", "r", encoding="utf8") as f:
    intents = json.load(f)
words = pickle.load(open('pkl_w/words_conan_dub.pkl','rb'))
labels = pickle.load(open('pkl_l/labels_conan_dub.pkl','rb'))

def bank_of_words(s,words, show_details=True):
    bag_of_words = [0 for _ in range(len(words))]
    sent_words = nltk.word_tokenize(s)
    sent_words = [lemmatizer.lemmatize(word.lower()) for word in sent_words]
    for sent in sent_words:
        for i,w in enumerate(words):
            if w == sent:
                bag_of_words[i] = 1
    return np.array(bag_of_words)

def predict_label(s, model):
    # filtering out predictions
    pred = bank_of_words(s, words,show_details=False)
    response = model.predict(np.array([pred]))[0]
    ERROR_THRESHOLD = 0.25
    final_results = [[i,r] for i,r in enumerate(response) if r>ERROR_THRESHOLD]
    final_results.sort(key=lambda x: x[1], reverse=True)
    return_list = []
    for r in final_results:
        return_list.append({"intent": labels[r[0]], "probability": str(r[1])})
    return return_list

def Response(ints, intents_json):
    tags = ''
    response = '' 
    try: 
        tags = ints[0]['intent']
        list_of_intents = intents_json['intents']
        for i in list_of_intents:
            if(i['tag']== tags):
                response = random.choice(i['responses'])
                break
    except IndexError:
        response = "Oprosti, ali ja nemam podatke o tome."
    return response

def chatbot_response(msg, model):
    ints = predict_label(msg, model)
    response = Response(ints, intents)
    return response

def chat_conan_dub():
    con2 = 0
    con3 = 0
    while True:
        inp = '' 
        if con2 == 0:
            control = input('\n Do want to use speech option? Enter "yes" or "no".\n ')
            if control.lower() == 'yes':
                con2 = 1
            elif control.lower() == 'no':
                con2 = 2
        if con2 == 1:
            if con3 == 3:
                print("\n Bot: Oprosti, ali ovaj razgovor je gotov. \n")
                hrvatski_voice("Oprosti, ali ovaj razgovor je gotov.")
                time.sleep(5)
                inp = 'exit'
            else:
                inp = speech_to_text()
        elif con2 == 2:
            if con3 == 3:
                print("\n Bot: Oprosti, ali ovaj razgovor je gotov. \n")
                hrvatski_voice("Oprosti, ali ovaj razgovor je gotov.")
                time.sleep(5)
                inp = 'exit'
            else:
                inp = input("You: ")
        if inp.lower() == 'quit' or inp.lower() == 'exit':
            print('\n back to the Conan Category\n ')
            male_voice('Back to the conan category')
            time.sleep(3)
            break
        elif inp.lower() == 'intro':
            winsound.PlaySound(None, winsound.SND_PURGE)
            print('\n Puštam Conan Uvodnu špicu sa youtube.com\n ')
            hrvatski_voice('Puštam konan Uvodnu špicu sa jutjuba')
            time.sleep(5)
            winsound.PlaySound('intros/conan_intro_dub.wav', winsound.SND_ASYNC)
        elif inp.lower() == 'stop':
            winsound.PlaySound(None, winsound.SND_PURGE)
            print('')
        else:
            response = chatbot_response(inp, model)
            winsound.PlaySound(None, winsound.SND_PURGE)
            if response == "Oprosti, ali ja nemam podatke o tome.":
                con3 += 1
                if con3<3:
                    print("\n BOT:" + response + '\n')
                    hrvatski_voice(response)
            else: 
                con3 = 0
                print("\n BOT:" + response + '\n')
                hrvatski_voice(response)