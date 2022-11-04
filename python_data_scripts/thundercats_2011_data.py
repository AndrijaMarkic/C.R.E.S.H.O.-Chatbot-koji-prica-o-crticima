from sklearn.naive_bayes import MultinomialNB
from sklearn.feature_extraction.text import CountVectorizer
from stt_tts.tts import male_voice
import time
from stt_tts.stt import speech_to_text

labels = []
questions = []

for line in open('databases/Thundercats 2011/thundercats q.txt', encoding='utf8'):
    labels.append(line.strip().split(' ')[-1])
    questions.append(' '.join(line.split(' ')[:-1]))

answers = []

for line in open('databases/Thundercats 2011/thundercats a.txt', encoding='utf8'):
    answers.append(line.strip())

bow_vectorizer = CountVectorizer()
training_vectors = bow_vectorizer.fit_transform(questions)

classifier = MultinomialNB()
classifier.fit(training_vectors, labels)

def start_chat_thundercats():
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
            print('\n back to the main menu\n ')
            male_voice('Back to the main menu')
            time.sleep(5)
            break
        elif user_response=='intro':
            print("\n Sorry but this show doesn't have theme song\n")
            male_voice("Sorry but this show doesn't have theme song")
        elif user_response=='dub':
            print("\n Sorry but this show doesn't have Croatian dub, but my creator rly like to see someone made it.\n")
            male_voice("Sorry but this show doesn't have Croatian dub, but my creator rly like to see someone made it.")
        else:
            reply = generate_response(user_response)+'\n'
            print(f'\n {reply}')
            male_voice(reply)
    return

def generate_response(sentence):
    input_vector = bow_vectorizer.transform([sentence])
    predict = classifier.predict(input_vector)
    #print(predict)
    index = int(predict[0])
    #print(index)
    return answers[index-1]