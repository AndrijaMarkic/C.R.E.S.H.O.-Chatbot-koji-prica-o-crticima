from sklearn.naive_bayes import MultinomialNB
from sklearn.feature_extraction.text import CountVectorizer
import winsound
import time
from stt_tts.tts import male_voice , hrvatski_voice
from python_data_scripts.conan_dub_data import start_chat_conan_dub
from stt_tts.stt import speech_to_text
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *

labels = []
questions = []

for line in open('databases/Conan the Adventurer/conan q.txt', encoding='utf8'):
    labels.append(line.strip().split(' ')[-1])
    questions.append(' '.join(line.split(' ')[:-1]))

answers = []

for line in open('databases/Conan the Adventurer/conan a.txt', encoding='utf8'):
    answers.append(line.strip())

bow_vectorizer = CountVectorizer()
training_vectors = bow_vectorizer.fit_transform(questions)

classifier = MultinomialNB()
classifier.fit(training_vectors, labels)

def start_chat_conan(user_response):
    if user_response=='dub':
        winsound.PlaySound(None, winsound.SND_PURGE)
        print('\n Odabrali ste Conan Pustolov Hrvatska Sinkronizacija. Što želite znati o sinkronizaciji?\n ')
        hrvatski_voice('Odabrali ste konan Pustolov Hrvatska Sinkronizacija. Što želite znati o sinkronizaciji?')
        print(' Enter any subject from this cartoon.\n Enter "exit" to back to the conan category\n ')
        start_chat_conan_dub()
    else:
        winsound.PlaySound(None, winsound.SND_PURGE)
        reply = generate_response(user_response)+'\n'
        print(f'\n {reply}')
        male_voice(reply)
        return reply

def generate_response(sentence):
    input_vector = bow_vectorizer.transform([sentence])
    predict = classifier.predict(input_vector)
    #print(predict)
    index = int(predict[0])
    #print(index)
    return answers[index-1]