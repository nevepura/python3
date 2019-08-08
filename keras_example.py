from keras.models import Sequential
from keras.layers import Dense
import numpy as np

print('trying keras')


x_train = np.random.randn(1, 32)
y_train = np.array([0.3])
print(x_train.shape)
print(y_train.shape)


model = Sequential()
model.add(Dense(units = 32, input_shape=(32,), activation = 'relu'))
model.add(Dense(units = 32, activation = 'relu'))
model.add(Dense(units = 16, activation = 'relu'))
model.add(Dense(units = 8, activation = 'relu'))
model.add(Dense(units = 1, activation = 'sigmoid'))

model.compile(loss = 'binary_crossentropy', optimizer = 'sgd', metrics = ['accuracy'])

model.fit(x_train, y_train, epochs = 100, batch_size = 2)
