from sklearn.naive_bayes import MultinomialNB
from sklearn.feature_extraction.text import CountVectorizer
from stt_tts.tts import female_voice, hrvatski_voice
import winsound
import time
from python_data_scripts.mlp_dub1_data import start_chat_mlp_dub1
from python_data_scripts.mlp_dub2_data import start_chat_mlp_dub2
from stt_tts.stt import speech_to_text

labels = []
questions = []

for line in open('databases/My Little Pony Friendship is Magic/mlp q.txt', encoding='utf8'):
    labels.append(line.strip().split(' ')[-1])
    questions.append(' '.join(line.split(' ')[:-1]))

answers = []

for line in open('databases/My Little Pony Friendship is Magic/mlp a.txt', encoding='utf8'):
    answers.append(line.strip())

bow_vectorizer = CountVectorizer()
training_vectors = bow_vectorizer.fit_transform(questions)

classifier = MultinomialNB()
classifier.fit(training_vectors, labels)

def start_chat_mlp():
    con2 = 0
    while True:
        user_response = '' 
        if con2 == 0:
            control = input('\n Do want to use speech option? Enter "yes" or "no".\n ')
            if control.lower() == 'yes':
                con2 = 1
            elif control.lower() == 'no':
                con2 = 2
        if con2 == 1:
            user_response = speech_to_text()
        elif con2 == 2:
            user_response = input()
        if user_response=='exit' or user_response=='quit':
            winsound.PlaySound(None, winsound.SND_PURGE)
            print('\n back to the main menu\n ')
            female_voice('Back to the main menu')
            time.sleep(4)
            break
        elif user_response=='intro':
            winsound.PlaySound(None, winsound.SND_PURGE)
            print('\n Playing My Little Pony G04 Theme Song from Youtube.com\n ')
            female_voice('playing My Little Pony G4 Theme Song from youtube dot com')
            time.sleep(4)
            winsound.PlaySound('intros/mlp_g04_intro.wav', winsound.SND_ASYNC)
        elif user_response=='stop':
            winsound.PlaySound(None, winsound.SND_PURGE)
            print('')
        elif user_response=='dub':
            winsound.PlaySound(None, winsound.SND_PURGE)
            print('\n This show haves 3 croatian dubs. What kind of dub you want to know about?\n 1. Novi Mediji Zg\n 2. Demo Project 6\n 3. Livada Produkcija\n ')
            female_voice('This show haves 3 croatian dubs. What kind of dub you want to know about?')
            hey = input()
            if hey == '1':
                print("\n Sorry I don't have data about this dub. Or doesn't exist or my creator don't want you to know something about it.\n")
                female_voice("Sorry I don't have data about this dub. Or doesn't exist or my creator don't want you to know something about it.")
            elif hey == '2':
                print('\n Odabrali ste MLP 1st Hrvatska Sinkronizacija. Što želite znati o sinkronizaciji?\n ')
                hrvatski_voice('Odabrali ste MOj Mali Poni prva Hrvatska Sinkronizacija. Što želite znati o sinkronizaciji?')
                print(' Enter any subject from this cartoon.\n Enter "exit" to back to the my little pony category\n ')
                start_chat_mlp_dub1()
            elif hey == '3':
                print('\n Odabrali ste MLP 2nd Hrvatska Sinkronizacija. Što želite znati o sinkronizaciji?\n ')
                hrvatski_voice('Odabrali ste MOj Mali Poni druga Hrvatska Sinkronizacija. Što želite znati o sinkronizaciji?')
                print(' Enter any subject from this cartoon.\n Enter "exit" to back to the my little pony category\n ')
                start_chat_mlp_dub2()
            else:
                print('\n Sorry I dont have that option.\n ')
                female_voice('Sorry I dont have that option.')
        else:
            winsound.PlaySound(None, winsound.SND_PURGE)
            reply = generate_response(user_response)+'\n'
            print(f'\n {reply}')
            female_voice(reply)
    return

def generate_response(sentence):
    input_vector = bow_vectorizer.transform([sentence])
    predict = classifier.predict(input_vector)
    #print(predict)
    index = int(predict[0])
    #print(index)
    return answers[index-1]