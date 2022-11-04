from sklearn.naive_bayes import MultinomialNB
from sklearn.feature_extraction.text import CountVectorizer
import winsound
import time
from stt_tts.tts import hrvatski_voice, male_voice
from stt_tts.stt import speech_to_text

labels = []
questions = []

for line in open('databases/Pokemon/pokemon q-dub.txt', encoding='utf8'):
    labels.append(line.strip().split(' ')[-1])
    questions.append(' '.join(line.split(' ')[:-1]))

answers = []

for line in open('databases/Pokemon/pokemon a-dub.txt', encoding='utf8'):
    answers.append(line.strip())

bow_vectorizer = CountVectorizer()
training_vectors = bow_vectorizer.fit_transform(questions)

classifier = MultinomialNB()
classifier.fit(training_vectors, labels)

def start_chat_pokemon_dub():
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
            print('\n back to the Pokemon category\n ')
            male_voice('Back to the pokemon category')
            break
        elif user_response=='intro':
            winsound.PlaySound(None, winsound.SND_PURGE)
            print('\n Puštam Pokemon Uvodnu špicu sa youtube.com\n ')
            hrvatski_voice('Puštam Pokemon Uvodnu špicu sa jutjuba')
            time.sleep(5)
            winsound.PlaySound('intros/pokemon_s01_intro_dub.wav', winsound.SND_ASYNC)
        elif user_response=='stop':
            winsound.PlaySound(None, winsound.SND_PURGE)
            print('')
        else:
            winsound.PlaySound(None, winsound.SND_PURGE)
            reply = generate_response(user_response)+'\n'
            print(f'\n {reply}')
            hrvatski_voice(reply)
    return

def generate_response(sentence):
    input_vector = bow_vectorizer.transform([sentence])
    predict = classifier.predict(input_vector)
    #print(predict)
    index = int(predict[0])
    #print(index)
    return answers[index-1]