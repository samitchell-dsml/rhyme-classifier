'''
A custom Dataset class for our word data
'''

import os
import pandas as pd
from torch.utils.data import Dataset


class WordDataset(Dataset):
    def __init__(self, data_file):
        df = pd.read_csv(data_file)
        
        self.length = len(df)
        self.word1 = df['Word1']
        self.word2 = df['Word2']
        self.rhyme = df['Rhyme']

    def __len__(self):
        return self.length

    def __getitem__(self, index):
        return (self.word1[index], self.word2[index], self.rhyme[index])

data_file = os.path.abspath(os.path.join(os.path.dirname(__file__), 'data/test.csv'))
dataset = WordDataset(data_file)

print(len(dataset))
print(dataset[0])