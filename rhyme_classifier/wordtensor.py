import numpy as np
import torch

def chrvec(char):
    """Creates a row-vector representing the letter's position

    Parameters
    ----------
    letter: str 
        A lowercase letter from the latin alphabet

    Returns
    -------
    numpy array
        a 26 element row with a 1 in the position the letter holds
        in the alphabet
    """

    i = ord(char) - ord('a')
    x = np.zeros(26)
    x[i] = 1.0

    return x

def wordtensor(word):
    '''Returns a tensor representing the word 
    
    The longest word in the unix words list has 24 letters, so
    we take this as the maximum number of rows needed for our
    vector representation of a word. Longer words in the Oxford
    dictionary are weird medical terms that we will not allow in
    the rhyme classifier

    Parameters
    ----------
    word: str
        A word in the English language of no more than 24 
        lowercase letters

    Returns
    -------
    torch tensor
        An tensor of shape (24, 26) representing the word as a
        matrix for processing in a neural network
    '''

    vec = np.zeros((24,26))

    for i in range (0,len(word)):
        vec[i] = chrvec(word[i])

    return torch.from_numpy(vec)