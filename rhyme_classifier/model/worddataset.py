'''
Defines a custom Dataset class for our word data
'''

import pandas as pd
import torch
from torch.utils.data import Dataset
from wordtensor import wordtensor


class WordDataset(Dataset):
    '''
    A class which extends Dataset specific to our word datasets
    '''

    def __init__(self, data_file):
        '''
        Initialises the object by creating lists of tensors of
        words

        Paramters
        ---------
        data_file : the path of the csv data file
        '''
        df = pd.read_csv(data_file)
        words1 = [wordtensor(str(word)) for word in df['Word1']]
        words2 = [wordtensor(str(word)) for word in df['Word2']]
        words = zip(words1, words2)
        
        self.length = len(df)
        self.x = [torch.cat((word1, word2), 0) for word1, word2 in words]
        self.y = df['Rhyme']

    def __len__(self):
        '''
        Gives the size of the dataset
        '''
        return self.length

    def __getitem__(self, index):
        '''
        Gets an item in the dataset.

        Parameters
        ----------
        index : int
            The index of the item
        '''

        return (self.x[index], self.y[index])
