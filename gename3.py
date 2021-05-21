import numpy as np
from keras.models import Sequential
from keras.layers import Dense
from keras.layers import Dropout
from keras.layers import LSTM
from keras.callbacks import ModelCheckpoint
from keras.utils import np_utils

# load ascii text and covert to lowercase
filename = "data/names.txt"
raw_text = open(filename).read()
raw_text = raw_text.lower()

chars = sorted(list(set(raw_text)))
char_to_int = dict((c, i) for i, c in enumerate(chars))
int_to_char = dict((i, c) for i, c in enumerate(chars))
names = raw_text.split()

maxLen = 0
step = 3
for n in names:
    maxLen = max(len(n), maxLen)

text = '\n'.join(names)
sentences = []
next_chars = []
for i in range(0, len(text) - maxLen, step):
    sentences.append(text[i: i + maxLen])
    next_chars.append(text[i + maxLen])
print('Number of sequences:', len(sentences))
print('First 10 sequences and next chars:')
for i in range(10):
    print('[{}]:[{}]'.format(sentences[i], next_chars[i]))
exit()

dataX = []
dataY = []
ly = 0.
for n in names:
    x = np.zeros(maxLen)
    for i in range(len(n)):
        x[i] = float(char_to_int[n[i]])
    dataX.append(x)
    dataY.append(0.)

X = np.reshape(dataX, (len(dataX), maxLen, 1))

X = X/float(len(chars))
y = np_utils.to_categorical(dataY)
print(X)
print(y)

# define the LSTM model
model = Sequential()
model.add(LSTM(256, input_shape=(X.shape[1], X.shape[2])))
model.add(Dropout(0.2))
model.add(Dense(y.shape[1], activation='softmax'))
model.compile(loss='categorical_crossentropy', optimizer='adam')


filepath="weights-improvement-{epoch:02d}-{loss:.4f}.hdf5"
checkpoint = ModelCheckpoint(filepath, monitor='loss', verbose=1, save_best_only=True, mode='min')
callbacks_list = [checkpoint]
model.fit(X, y, epochs=8, batch_size=128, callbacks=callbacks_list)

# pick a random seed
start = np.random.randint(0, len(dataX)-1)
pattern = dataX[start].tolist()
print("Seed:")
print("\"", ''.join([int_to_char[value] for value in pattern]), "\"")
print(type(dataX))
print(type(pattern))
# generate characters
for i in range(25):
	x = np.reshape(pattern, (1, len(pattern), 1))
	x = x / float(len(chars))
	prediction = model.predict(x, verbose=0)
	index = np.argmax(prediction)
	result = int_to_char[index]
	seq_in = [int_to_char[value] for value in pattern]
	print(result)
    #pattern = np.append(pattern, index)
	pattern.append(index)
	pattern = pattern[1:len(pattern)]
print("\nDone.")