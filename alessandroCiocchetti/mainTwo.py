# coding: utf-8

import re
from classWordFrequency import Frequency

def mainTwo():

    txt = input('Digita il nome del file .txt da leggere (e.g. libro.txt): ')
    #creo un oggetto della classe Frequency
    text = Frequency(txt)

    print("\n---------------------------------Row Data from txt------------------------------------------\n")
    #visualizzo il contenuto del testo in una lista di stringhe (prime 30 righe)
    print(text.content[:30])

    print("\n----------------------------------Cleaned Data splitted in words-----------------------------------------\n")
    #rimuovo dalle stringhe i caratteri speciali e splitto in parole singole
    #salvando il risultato nella variabile "words" + stampa delle prime 100 parole

    words = text.clean_data()
    print(words[:100])

    print("\n----------------------------------Most Common Words ordered by frequency-----------------------------------------\n")
    #salvo in una variabile "mc_30" il risultato del metodo mostCommon() chiamato sull'oggetto text
    #e stampo il risultato
    mc_30 = text.mostCommon(30)
    print(mc_30)

if __name__ == '__main__':
    mainTwo()
