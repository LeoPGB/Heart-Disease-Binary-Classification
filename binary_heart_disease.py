import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import tensorflow as tf
from tensorflow import keras
from tensorflow.keras import layers

#https://www.kaggle.com/datasets/cherngs/heart-disease-cleveland-uci
df = pd.read_csv('/content/heart.csv')
df.head()

df.shape

df.count()

df.describe()

df.info()

df.isna().sum()

plt.figure(figsize=(12,12))
sns.heatmap(df.corr(), annot=True)
plt.show()

a = df['condition'].map({0:'No disease', 1:'Disease'})
sns.countplot(x=df['sex'].map({0:'Female', 1:'Male'}), hue=(a))

x = df.drop('condition', axis=1)
y = df['condition']

x.head()

y.head()

print(x.shape)
print(y.shape)

model = keras.Sequential()
model.add(layers.Dense(13, activation = 'relu'))
model.add(layers.Dense(1, activation = 'sigmoid'))
model.compile(loss='binary_crossentropy', optimizer='adam', metrics=['accuracy'])
history = model.fit(x, y, validation_split=0.25, epochs=150)

model.summary()

plt.plot(history.history['loss'])
plt.plot(history.history['val_loss'])
plt.title('Model Loss')
plt.xlabel('Epoch')
plt.ylabel('Loss')
plt.legend(['train', 'test'], loc='upper right')

plt.plot(history.history['accuracy'])
plt.plot(history.history['val_accuracy'])
plt.title('Model Accuracy')
plt.xlabel('Epoch')
plt.ylabel('Accuracy')
plt.legend(['train', 'test'], loc='upper right')

x_pred = ([[67,1,0,125,254,1,1,163,0,0.2,1,2,3]])
x_pred = np.array(x_pred, dtype=np.float64)
y_pred = (model.predict(x_pred)>0.5).astype('int32')
print(y_pred[0][0])

sample = df.sample(n=35)
x_pred = sample.drop('condition', axis=1)
y_true = sample['condition'].to_numpy().astype('int32')
y_pred = (model.predict(x_pred)>0.6).astype('int32').flatten()

a = 0
b = len(y_true)
for i in range(b):
  if (y_pred[i] == y_true[i]):
    a = a + 1
print('Values from Samples: ', y_pred)
print('        True Values: ', y_true)
print('Prediction Accuracy: ', (a*100/b), '%')

