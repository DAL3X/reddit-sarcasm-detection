# sarcasm detection in reddit comments

Detecting sarcasm in reddit comments using added features, text vectorization and LSTM RNNs.
Machine learning project for 'laboratory for applied machine learning algorithms' course at KIT.

[kaggle post](https://www.kaggle.com/danofer/sarcasm)

## order of execution
* feature_engineering.ipynb
* machine_learning.ipynb
* visualization.ipynb

## used datasets
* [test-balanced.csv.bz2](https://nlp.cs.princeton.edu/SARC/0.0/main/test-balanced.csv.bz2) as 'dataset/test-balanced.csv'
* [train-balanced.csv.bz2](https://nlp.cs.princeton.edu/SARC/0.0/main/train-balanced.csv.bz2) as 'dataset/train-balanced.csv'

![dataset](https://github.com/phil-kit/reddit-comment-lama/raw/main/graphs/dataset_head.png)

## model flow
### general
![Flow 1](https://github.com/phil-kit/reddit-comment-lama/raw/main/graphs/model_flow.png)


### text
![Flow 1](https://github.com/phil-kit/reddit-comment-lama/raw/main/graphs/text_flow.png)

## results
![results](https://github.com/phil-kit/reddit-comment-lama/raw/main/graphs/compare_models.png)

## proof of concept - real world implementation
* run 'am_i_sarcastic.py' for a simple demonstration. It uses 'models/only_comment' since we don't have any metadata for text input.
![example](https://github.com/phil-kit/reddit-comment-lama/raw/main/graphs/am_i_sarcastic.png)

Simon Bothe, Philip Schröder

2022
