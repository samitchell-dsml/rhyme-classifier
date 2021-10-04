from nltk.corpus import cmudict
import os
import rhymes

def clean_cmudict():
    clean_words = []
    dict_words = list(cmudict.dict().keys())

    for word in dict_words:
        bad_chr = False

        for chr in word:
            if chr in ["'", '.'] or chr.isnumeric():
                bad_chr = True

        if not bad_chr:
            clean_words.append(word)

    return clean_words

def write_line(line, file):
    with open(file, 'a') as f:
        f.write(line + '\n')    

def generate_raw_data(words):
    data_path = os.path.join(os.path.dirname(__file__), 'data')
    rhyme_pairs_file = os.path.join(data_path, 'rhymes.csv')
    no_rhyme_pairs_file = os.path.join(data_path, 'notrhymes.csv')

    for i in range(0, len(words)):
        for j in range(i+1, len(words)):
            print(i,j)
            
            rhyme = rhymes.rhymes(words[i], words[j])
            line = ', '.join([words[i], words[j]])
        
            if rhyme:
                write_line(line, rhyme_pairs_file)
            else:
                write_line(line,no_rhyme_pairs_file)
    
    print('\n Done. \n')

generate_raw_data(clean_cmudict())