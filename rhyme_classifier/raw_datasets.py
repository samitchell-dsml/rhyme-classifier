import json
import os
from nltk.corpus.reader import wordlist
import numpy as np
import random

data_path = os.path.join(os.path.dirname(__file__), 'data')
dict_file = os.path.join(data_path, 'rhyming_dict.json')
train_csv = os.path.join(data_path, 'train.csv')
test_csv = os.path.join(data_path, 'test.csv')

def generate_dataset(n,train):
    '''Generates a dataset for the rhyme-classifier

    Generates a collection of n word pairs and a boolean value
    for whether they rhyme. The number n is partitioned into an 
    approximate ratio of non-rhymes : rhymes = 9 : 1. The rhyming 
    dictionary is filtered to remove sounds containing one word.

    Parameters
    ----------

    n : int
        The number of elements in the dataset

    train : bool
        If true, write to train.csv file
        If false, write to test.csv
    
    '''
    if train:
        write_file = train_csv
    else:
        write_file = test_csv
    
    with open(dict_file, 'r') as file:
        rhyme_dict = json.load(file)


    # filter out all sounds with only one word
    rhyme_items = [(s,l) for s,l in list(rhyme_dict.items()) if len(l) > 1]

    random.seed()

    for i in range(0, n):
        # get a random number between 0 and 9, if its 0 we make a
        # rhyming pair
        rhyme_rand = int(10*random.random())


        if rhyme_rand == 0:
            sound = int(len(rhyme_items) * random.random())
            word_list = rhyme_items[sound][1]

            rand1 = int(len(word_list) * random.random())
            rand2 = int(len(word_list) * random.random())

            word1 = word_list[rand1]
            word2 = word_list[rand2]
            
            line = ', '.join([word1, word2, '1'])
            
            with open(write_file, 'a') as file:
                file.write(line + '\n')
              
        else:
            sound1 = int(len(rhyme_items) * random.random())
            rem_sounds = [(s,l) for s,l in rhyme_items if s != rhyme_items[sound1][0]]
            sound2 = int(len(rem_sounds) * random.random())

            list1 = rhyme_items[sound1][1]
            list2 = rhyme_items[sound2][1]

            rand1 = int(len(list1)*random.random())
            rand2 = int(len(list2)*random.random())

            word1 = list1[rand1]
            word2 = list2[rand2]

            line = ', '.join([word1, word2, '0'])

            with open(write_file, 'a') as file:
                file.write(line + '\n')

if __name__ == '__main__':
    train = generate_dataset(50000, True)
    test = generate_dataset(10000, False)



    

    