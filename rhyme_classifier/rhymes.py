from nltk.corpus import cmudict

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

    pron = ' '.join(pron)

    rhyme_sound = 'No rhyme sound'

    for i in range(len(pron) - 1, -1, -1):
        if pron[i][-1] in ['1', '2']: # stressed vowels end in 1 or 2 in encoding
            rhyme_sound = pron[i:]
            break

    return rhyme_sound

def rhymes(word1, word2):
    '''Tests whether two words rhyme

    Parameters
    ----------
    word1: str
        The first word to be tested for rhyming

    word2: str
        The second word to be tested for rhyming
    
    Returns
    -------
    int
        1 if the words rhyme, 0 if they don't
    '''

    rhyme = 0

    for pron1 in cmudict.dict()[word1]:
        for pron2 in cmudict.dict()[word2]:
            if rhyme_sound(pron1) == rhyme_sound(pron2):
                rhyme = 1
                break

    return rhyme
