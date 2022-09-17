import sys

import numpy as np
np.random.seed(1)

f = open('reviews.txt')
raw_reviews = f.readlines()
f.close()

f = open('labels.txt')
raw_labels = f.readlines()
f.close()

tokens = list(map(lambda x: set(x.split(" ")), raw_reviews))

alpha, iterations = (0.01, 2)
hidden_size = 100

vocab = set()

for sent in tokens:
    for word in sent:
        if len(word) > 0:
            vocab.add(word)

vocab = list(vocab)

word2index = {}
for i, word in enumerate(vocab):
    word2index[word] = i
            
input_dataset = list()
for sent in tokens:
    sent_indices = list()
    for word in sent:
        try:
            sent_indices.append(word2index[word])
        except:
            ""
    input_dataset.append(list(set(sent_indices)))

target_dataset = list()
for label in raw_labels:
    if label == 'positive\n':
        target_dataset.append(1)
    else:
        target_dataset.append(0)


weights_0_1 = 0.2 * np.random.random( (len(vocab), hidden_size)) - 0.1
weights_1_2 = 0.2 * np.random.random( (hidden_size, 1)) - 0.1 


from collections import Counter
import math 

def similar(target='beautiful'):
    target_index = word2index[target]
    scores = Counter()
    for word,index in word2index.items():
        raw_difference = weights_0_1[index] - (weights_0_1[target_index])
        squared_difference = raw_difference * raw_difference
        scores[word] = -math.sqrt(sum(squared_difference))

    return scores.most_common(10)
    
print(similar("beautiful"))
print()
print(similar("terrible"))