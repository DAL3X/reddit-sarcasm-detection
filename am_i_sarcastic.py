# example for real world implementation. proof of concept

print('starting...')
from os import environ
environ["CUDA_VISIBLE_DEVICES"] = "-1" # disable GPU for simple prediction
from tensorflow.keras.models import load_model

print('loading model for prediction...')
model = load_model(f'models/only_comment') #load model
print('done.\n')

while True:
    print('\033[95menter yout text:\033[94m ', end='')
    text = input() # prompt for input
    if (text != ''): # prediction crashes with empty string
        prediction = model.predict([text])[0][0] # get prediction
        sarcasm = True if (prediction>.5) else False
        if sarcasm: print(f'\033[95m> your input was sarcasm (confidence: {int(prediction*100)}%)\033[94m\n')
        else: print(f'\033[95m> your input was not sarcasm (confidence: {int((1-prediction)*100)}%)\033[94m\n')