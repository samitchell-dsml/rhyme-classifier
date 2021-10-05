'''
Gives a function to build a rhyming dictionary indexed by the phoneme
string that makes the sound of the rhyme
'''

from nltk.corpus import cmudict
import json

def clean(word):
    '''
    Determines whether a word contains an apostrophe, period, or number

    Parameters
    ----------
    word : str
        The word to be checked for an apostrophe, period or number

    Returns
    -------
    bool
        True if word is free from unwanted characters
    '''
    clean = True

    for chr in word:
        if ord(chr) not in range(ord('a'), ord('z')+27):
            clean = False
            break

    return clean

def rhyme_sound(pron):
    '''
    Gives the string of phonemes which creates the rhyme sound 
    
    Parameters
    ----------
    pron: list
        A list of phonemes which makes up the pronounciation of a word

    Returns
    -------
    str
        a string of the phonemes which make the rhyme sound
    '''

    rhyme_sound = None

    for i in range(len(pron) - 1, -1, -1):
        if pron[i][-1] in ['1', '2']: # stressed vowels end in 1 or 2 in encoding
            rhyme_sound = ' '.join(pron[i:])
            break

    return rhyme_sound

def build_rhyme_dict(file):
    '''
    Creates a dictionary of rhyming words and saves it to file.

    Ignores words with no rhyme and words with punctuation or numbers.

    Parameters
    ----------
    file : str
        The path of the location to save the dictionary
    '''

    rhyme_dict = {}

    for word, pron in cmudict.entries():
        if clean(word):
            sound = rhyme_sound(pron)

            if sound != None:
                if sound in rhyme_dict.keys():
                    if word not in rhyme_dict[sound]:
                        rhyme_dict[sound].append(word)
                else:
                    rhyme_dict[sound] = [word]
    
    with open(file, 'w') as f:
        json.dump(rhyme_dict, f)
