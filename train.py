import nltk
from nltk.stem import WordNetLemmatizer
lemmatizer = WordNetLemmatizer()
import numpy as np
from keras.models import Sequential
from keras.layers import Dense, Dropout , Activation, Flatten , Conv2D, MaxPooling2D
from keras.optimizers import SGD
import random
import json
import pickle

words=[]
labels = []
docs = []
ignore_list = ['?', '!']

conan = "databases/Conan the Adventurer/conan.json"
conan_dub = "databases/Conan the Adventurer/conan_dub.json"
mlp = "databases/My Little Pony Friendship is Magic/mlp.json"
mlp_dub1 = "databases/My Little Pony Friendship is Magic/mlp_dub1.json"
mlp_dub2 = "databases/My Little Pony Friendship is Magic/mlp_dub2.json"
pokemon = "databases/Pokemon/pokemon.json"
pokemon_dub = "databases/Pokemon/pokemon_dub.json"
spongebob = "databases/SpongeBob/spongebob.json"
spongebob_dub = "databases/SpongeBob/spongebob_dub.json"
thundercats = "databases/Thundercats 2011/thundercats.json"

with open(thundercats, "r", encoding="utf8") as f:
    intents = json.load(f)

for intent in intents['intents']:
    for pattern in intent['patterns']:

        #tokenize each word
        word_token = nltk.word_tokenize(pattern)
        words.extend(word_token)
        #add documents in the corpus
        docs.append((word_token, intent['tag']))

        # add to our labels list
        if intent['tag'] not in labels:
            labels.append(intent['tag'])

# lemmatize each word, and sort words by removing duplicates:
words = [lemmatizer.lemmatize(word.lower()) for word in words if word not in ignore_list]
words = sorted(list(set(words)))
# sort labels:
labels = sorted(list(set(labels)))

pickle.dump(words,open('pkl_w/words_thundercats.pkl','wb'))
pickle.dump(labels,open('pkl_l/labels_thundercats.pkl','wb'))

# creating our training data:
training_data = []
# creating an empty array for our output (with size same as length of labels):
output = [0]*len(labels)

for doc in docs:
    bag_of_words = []
    pattern_words = doc[0]
    #lemmatize pattern words:
    pattern_words = [lemmatizer.lemmatize(word.lower()) for word in pattern_words]
    
    for w in words:
        if w in pattern_words:
            bag_of_words.append(1)
        else:
            bag_of_words.append(0)
            
    output_row = list(output)
    output_row[labels.index(doc[1])] = 1
    
    training_data.append([bag_of_words,output_row])

# convert training_data to numpy array and shuffle the data:
random.shuffle(training_data)
training_data = np.array(training_data)

# Now we have to create training list:
x_train = list(training_data[:,0])
y_train = list(training_data[:,1])
# Creating Model:

model = Sequential()
model.add(Dense(128, input_shape=(len(x_train[0]),), activation='relu'))
#model.add(Dropout(0.5))
model.add(Dense(64, activation='relu'))
#model.add(Dropout(0.5))
model.add(Dense(len(y_train[0]), activation='softmax'))

model.summary()

sgd_optimizer = SGD(lr=0.01, decay=1e-6, momentum=0.9, nesterov=True)
model.compile(loss='categorical_crossentropy', optimizer=sgd_optimizer, metrics=['accuracy'])

# fit the model 
history = model.fit(np.array(x_train), np.array(y_train), epochs=200, batch_size=5, verbose=1)

model.save('models/thundercats_chatbot_model.h5', history)
