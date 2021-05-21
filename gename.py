import keras
import numpy as np
from keras.models import Sequential
from keras.layers import Dense
from keras.layers import Dropout
from keras.layers import LSTM
from keras.callbacks import ModelCheckpoint, LambdaCallback
from keras.utils import np_utils
from keras.models import load_model
import random
# load ascii text and covert to lowercase
from Individu import Individu, meet

def showSociety(society):
    max_len_name = 0
    for i in society:
        max_len_name = max(max_len_name, len(i.name))
        print(i, i.opinions)

    header = "|" + ' ' * (max_len_name) + " |"
    sep = "+" + '-' * (max_len_name) + "-+"
    for i in society:
        sep += '-' * max(len(i.name), 4) + "-+"
        header += i.name + '-' * max(4 - len(i.name), 0) + " |"
        # header += "{0:^max_len_name}".format(i.name) + " |"
    print(sep)
    print(header)
    for i in society:
        #print(sep)
        s = "|" + i.name + ' ' * (max_len_name - len(i.name)) + " |"
        for j in society:
            if j.name in i.opinions.keys():
                s += str(i.opinions[j.name]) + ' ' * (max(len(j.name), 4) - len(str(i.opinions[j.name]))) + " |"
            else:
                s += '-' * max(len(j.name), 4) + " |"
        print(s)

    print(sep)
#import file to list
filename = "data/names.txt"
nameslist = open(filename).readlines()
nameslist = list(map(lambda s:s.lower().replace("\n", "."), nameslist))

#build dicts char and int
chars = sorted(list(set(".".join(nameslist))))
char_to_int = dict((c, i) for i, c in enumerate(chars))
int_to_char = dict((i, c) for i, c in enumerate(chars))

longestName = len(max(nameslist, key=len))
namesCount = len(nameslist)
char_dim = len(int_to_char)

X = np.zeros((namesCount, longestName, char_dim))
Y = np.zeros((namesCount, longestName, char_dim))

for i in range(namesCount):
    name = list(nameslist[i])
    for j in range(len(name)):
        X[i, j, char_to_int[name[j]]] = 1
        if j < len(name)-1:
            Y[i, j, char_to_int[name[j+1]]] = 1


def make_name(model):
    name = []
    x = np.zeros((1, longestName, char_dim))
    end = False
    i = 0

    while end == False:
        probs = list(model.predict(x)[0, i])
        probs = probs / np.sum(probs)
        index = np.random.choice(range(char_dim), p=probs)
        if i == longestName - 2:
            character = '.'
            end = True
        else:
            character = int_to_char[index]
        name.append(character)
        x[0, i + 1, index] = 1
        i += 1
        if character == '.':
            end = True

    #print(''.join(name))
    return ''.join(name)[:-1].capitalize()


def generate_name_loop(epoch, _):
    #if epoch % 5 == 0:
    print('Names generated after epoch %d:' % epoch)
    for i in range(5):
        make_name(model)
    print()


name_generator = LambdaCallback(on_epoch_end=generate_name_loop)

'''model = Sequential()
model.add(LSTM(128, input_shape=(longestName, char_dim), return_sequences=True))
model.add(Dense(char_dim, activation='softmax'))

filepath = "weights-improvement-{epoch:02d}-{loss:.4f}.hdf5"
checkpoint = ModelCheckpoint(filepath, monitor='loss', verbose=1, save_best_only=True, mode='min')

model.compile(loss='categorical_crossentropy', optimizer='adam')
model = load_model('lstm5_model.h5')
model.fit(X, Y, batch_size=64, epochs=50, callbacks=[name_generator, checkpoint], verbose=0)
model.save('names_model.h5')'''

model = load_model('names_model.h5')

noms = []
society = []
for i in range(random.randint(2, 40)):
    society.append(Individu(make_name(model)))
    noms.append(make_name(model))

print(society)
for i in range(100):
    meet(random.choice(society), random.choice(society))

showSociety(society)

