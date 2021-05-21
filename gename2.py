import keras
import numpy as np
from keras.models import Sequential
from keras.layers import Dense
from keras.layers import Dropout
from keras.layers import LSTM
from keras.layers import SimpleRNN
from keras.callbacks import ModelCheckpoint
from keras.utils import np_utils
from keras.models import load_model
from keras.utils import to_categorical
import random
# load ascii text and covert to lowercase
from Individu import Individu, meet

filename = "data/names.txt"

maxlength = 0
with open(filename) as fl:
    line = fl.readline()
    while line:
        maxlength = max(maxlength, len(line))
        line = fl.readline()

maxlength = 5
print(maxlength)

raw_text = open(filename).read()
raw_text = raw_text.lower()

points = "."*(maxlength - 1)
points = '.'
print(points)

#text = "....." + raw_text.replace("\n", ".....")
text = points + raw_text.replace("\n", points).replace("-", points)
chars = sorted(list(set(text)))
char_to_int = dict((c, i) for i, c in enumerate(chars))
int_to_char = dict((i, c) for i, c in enumerate(chars))

print(chars)

names = raw_text.split()
#dicname = dict((c, i) for i, c in enumerate(names))
maxLen = 0
for n in names:
    maxLen = max(len(n), maxLen)

dataX = []
dataY = []
#length = 6
step = 1
xi = 0
yi = xi  + maxlength
while(yi < len(text)):
    a = text[xi:xi + maxlength]
    X = []
    for x in text[xi:xi + maxlength]:
        X.append(char_to_int[x])
    y = float(char_to_int[text[yi]])
    dataX.append(X)
    dataY.append(float(char_to_int[text[yi]]))
    #print(a, X, " => ", text[yi], " ", y, "\t(", xi, ",", yi, ")")
    if(y == 0):
        xi = yi
        yi = xi + maxlength
    else:
        xi += step
        yi += step

X = np.reshape(dataX, (len(dataX), maxlength, 1))
X = X/float(len(chars))
y = np_utils.to_categorical(dataY)

#print(X)
#print(y)

# define the LSTM model
model = Sequential()
#model.add(LSTM(256, input_shape=(X.shape[1], X.shape[2])))
model.add(LSTM(400, input_shape=(X.shape[1], X.shape[2]), return_sequences=True))
model.add(Dropout(0.2))
model.add(LSTM(400, return_sequences=True))
model.add(Dropout(0.2))
model.add(LSTM(400))
model.add(Dropout(0.2))
model.add(Dense(y.shape[1], activation='softmax'))


filepath="weights-improvement-{epoch:02d}-{loss:.4f}.hdf5"
#filepath="weights-improvement-{epoch:02d}-{loss:.4f}.hdf5"
checkpoint = ModelCheckpoint(filepath, monitor='loss', verbose=1, save_best_only=True, mode='min')
callbacks_list = [checkpoint]

#model = load_model("weights-improvement-15-2.2817.hdf5")
opt = keras.optimizers.Adam(lr=0.001, epsilon=1e-3, amsgrad=True)
model.compile(loss='categorical_crossentropy', optimizer=opt)

model = load_model("weights-improvement-03-1.7358.hdf5")
#model = load_model(filepath)
model.fit(X, y, epochs=3, batch_size=128, callbacks=callbacks_list)
model.save('lstm_model.h5')
#model = load_model('lstm_model2.h5')
print("loaded")

def geNames(l = 100):
    names = []
    for i in range(l):
        namids = [0]
        namids.append(np.random.randint(char_to_int['a'], len(char_to_int)))
        index = -1
        inp = np.zeros(maxlength)
        while(index != char_to_int['.']):
            inp[-len(namids):] = namids[-maxlength:]
            x = np.reshape(inp, (1, len(inp), 1))
            x = x/float(len(chars))
            prediction = model.predict(x, verbose=0)
            index = np.argmax(prediction)
            namp = []
            for i in range(len(prediction[0])):
                namp.append(i)
            index = np.random.choice(namp, p=prediction[0])
            namids.append(index)
        name = ""
        for id in namids:
            name += int_to_char[id]
        print(name[1:-1].capitalize())
        names.append(name[1:-1].capitalize())
    return names

'''names = geNames(100)
f = random.randint(2, 8)
while len(names) > f:
    comp = names[:f]
    names = names[f:]
    for c in range(len(comp)):
        print(c + 1, comp[c])
    mode = int(input('Input:')) - 1
    names.append(comp[mode])
    print(names)
    f = random.randint(2, 8)'''

'''compNames = geNames(32)
f = random.randint(2, 8)
while len(compNames) > f:
    print(len(compNames), ":", compNames)
    dual = random.sample(compNames, 2)
    print(dual)
    mode = int(input('prob the second wins [0,10]:'))
    killed = dual[1]
    if(mode > random.randint(0,10)):
        killed = dual[0]
    compNames.remove(killed)
    print(killed, "has been removed")
    print()

print(compNames)'''
print('--------')
noms = geNames(random.randint(30, 50))
print(noms)
f = random.randint(2, 8)
while len(noms) > f:
    nomdict = []
    for n in noms:
        mode = int(input(n + ': prob he lives [0,10]:'))
        if (mode > random.randint(0, 10)):
            nomdict.append(n)
        else:
            print(n, " is dead")
            print()
    noms = nomdict
    individus = []
    for n in noms:
        i = Individu(n)
        individus.append(i)
        print(i)
        print(meet(i, random.choice(individus)))



print(noms)
print("\nDone.")

