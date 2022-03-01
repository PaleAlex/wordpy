# coding: utf-8

# Write a Python program, in a file called main.py,  that reads a text file whose name is provided by the user,
#and builds a data structure storing the frequency of the words in the file, using the following rules:

# 1. Lower case and Upper case should make no difference (i.e., Home and hoMe are the same word)
# 2. Punctuation are not considered to be words or part of a word, including hyphen (i.e., multi-words are two different words — “multi” and “words”)


import re

#chiedo all'utente il nome del file.
txt = input('Digita il nome del file .txt da leggere (e.g. libro.txt): ')

#leggo il file
with open(txt) as f:
    rows = f.readlines()

#sistemo la lista di stringhe trasformando tutto lowercase per gestire il fattore "case sensitive"
content = [row.lower() for row in rows[1:]]


#elimino dal testo i caratteri speciali e creo la lista pulita con tutte le parole del testo che mi interessano

#NB:
#tra le parole è presente la lettera "s"
#che può essere sia la terza persona del verbo essere ma anche il genitivo sassone... questa casistica
#per semplificazione non l'ho gestita

word_list = []
for c in range(len(content)):
    string_no_punctuation = re.sub("[^a-zA-Z]", " ", content[c])
    wl = string_no_punctuation.split()
    if wl and wl != ['volume', 'i'] and wl != ['chapter', 'i']:  #elimino elementi vuoti e quelli relativi ai paragrafi (specifici del testo dato per l'esame)
        word_list += wl


# struttura per immagazzinare la frequenza delle diverse parole
word_dict = {}

for w in word_list:
    word_dict[w] = word_dict.get(w, 0) + 1

word_dict = dict(sorted(word_dict.items(), key=lambda item: item[1], reverse = True))


# By using the data structure created in the previous exercise, write a Python function (keep it in main.py),
#called mostCommon(), that finds the most common words, i.e., it returns a list of word-frequency tuples, sorted in reverse order by frequency

def mostCommon(n):
    '''n = number of words to be returned'''
    dict_items = word_dict.items()
    first_n = list(dict_items)[:n]
    print(first_n)
