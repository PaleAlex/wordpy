# coding: utf-8

import re

class Frequency():
    '''
    parametri: txt --> nome (di tipo stringa) del file (in formato .txt) da elaborare

    attributi:
    - .content --> restituisce la lista grezza di elementi corrispondenti alle righe del txt letto
    - .word_list --> restituisce l'intera lista di parole contenute nel txt

    '''

    def __init__(self, txt):
        self.txt = txt
        self.get_data()

    def get_data(self):
        with open(self.txt) as f:
            rows = f.readlines()
        self.content = [row.lower() for row in rows[1:]]
        return self.content

    def clean_data(self):
        self.word_list = []
        for c in range(len(self.content)):
            string_no_punctuation = re.sub("[^a-zA-Z]", " ", self.content[c])
            wl = string_no_punctuation.split()
            if wl and wl != ['volume', 'i'] and wl != ['chapter', 'i']:
                self.word_list += wl
        return self.word_list

    def mostCommon(self, n):
        '''n = number of words to be returned'''
        self.clean_data()
        word_dict = {}

        for w in self.word_list:
            word_dict[w] = word_dict.get(w, 0) + 1

        word_dict = dict(sorted(word_dict.items(), key=lambda item: item[1], reverse = True))

        dict_items = word_dict.items()
        first_n = list(dict_items)[:n]
        return first_n
