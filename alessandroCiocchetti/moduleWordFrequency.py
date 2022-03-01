# coding: utf-8
import re

def get_data(txt):
    '''txt è il nome (di tipo stringa) del file (in formato .txt) da elaborare'''
    with open(txt) as f:
        rows = f.readlines()
    content = [row.lower() for row in rows[1:]]
    return content

def clean_data(data):
    '''
    parametro -->
    data = lista di elementi di tipo stringa

    '''
    word_list = []
    for c in range(len(data)):
        string_no_punctuation = re.sub("[^a-zA-Z]", " ", data[c])
        wl = string_no_punctuation.split()
        if wl and wl != ['volume', 'i'] and wl != ['chapter', 'i']:
            word_list += wl
    return word_list


def mostCommon(n, words):
    '''
    n = numero di parole da restituire nell'output, ordinate per frequenza decrescente
    words = lista di elementi di tipo stringa rappresentanti parole singole

    '''

    word_dict = {}

    for w in words:
        word_dict[w] = word_dict.get(w, 0) + 1

    word_dict = dict(sorted(word_dict.items(), key=lambda item: item[1], reverse = True))

    dict_items = word_dict.items()
    first_n = list(dict_items)[:n]
    return first_n
