'''
Gives a function to turn a word stored in a string into a tensor
for processing by a neural network.
'''

import torch

def chartensor(char):
    '''
    Creates a tensor of shape (26) representing the letter's position

    Parameters
    ----------
    letter : str 
        A lowercase letter from the latin alphabet

    Returns
    -------
    torch tensor
        a tensor of shape (26) with a 1 in the position the letter holds
        in the alphabet
    '''
    i = ord(char) - ord('a')
    x = torch.zeros((26,))
    x[i] = 1.0

    print(x.shape)

    return x

def wordtensor(word):
    '''
    Returns a tensor representing the word 
    
    The longest word in the unix words list has 24 letters, so
    we take this as the maximum number of rows needed for our
    vector representation of a word. Longer words in the Oxford
    dictionary are weird medical terms that we will not allow in
    the rhyme classifier

    Parameters
    ----------
    word : str
        A word in the English language of no more than 24 
        lowercase letters

    Returns
    -------
    torch tensor
        a tensor of shape (24, 26) representing the word as a
        matrix for processing in a neural network
    '''

    x = torch.zeros((24,26))

    for i in range (0,len(word)):
        x[i] = chartensor(word[i])

    return x