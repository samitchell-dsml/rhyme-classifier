from nltk.corpus import cmudict
import json
import os

def clean(word):
    '''Determines whether a word contains an apostrophe, period, or number

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
        if chr in ["'", '.'] or chr.isnumeric():
            clean = False
            break

    return clean

def rhyme_sound(pron):
    '''Gives the string of phonemes which creates the rhyme sound 
    
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

def build_rhyme_dict():
    '''Creates a dictionary of rhyming words

    Ignores words with no rhyme
        
    Returns
    -------
    dict
        a dictionary of rhyming words keyed by the phoneme string which
        gives the rhyming sound

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
    
    return rhyme_dict


if __name__ == '__main__':
    rhyme_dict = build_rhyme_dict()

    with open(os.path.join(os.path.dirname(__file__), 'data', 'rhyming_dict.json'), 'w') as file:
        json.dump(rhyme_dict, file)
