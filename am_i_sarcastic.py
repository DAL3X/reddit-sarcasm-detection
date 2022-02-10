# example for real world implementation. proof of concept

print('starting...')

# imports
import tensorflow as tf
from typing import *

# enables GPU VRAM growth, static allocation tends to crash Desktop programs
gpus = tf.config.experimental.list_physical_devices('GPU')
for gpu in gpus:
    tf.config.experimental.set_memory_growth(gpu, True)

print('loading model for prediction...')
model = tf.keras.models.load_model(f'models/only_comment')
print('done.\n')

while True:
    print('\033[95menter yout text:\033[94m ', end='')
    text = input()
    if (text != ''):
        prediction = model.predict([text])[0][0]
        sarcasm = True if (prediction>.5) else False
        if sarcasm: print(f'\033[95m> your input was sarcasm (confidence: {int(prediction*100)}%)\033[94m')
        else: print(f'\033[95m> your input was not sarcasm (confidence: {int((1-prediction)*100)}%)\033[94m')