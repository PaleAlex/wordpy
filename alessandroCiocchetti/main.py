# coding: utf-8
from moduleWordFrequency import *
def main():

    txt = input('Digita il nome del file .txt da leggere (e.g. libro.txt): ')

    print("\n---------------------------------Row Data from txt------------------------------------------\n")

    #chiamo get_data, salvo il risultato in una variabile "data" e visualizzo le prime 30 righe

    data = get_data(txt)
    print(data[:30])

    print("\n----------------------------------Cleaned Data splitted in words-----------------------------------------\n")

    ##chiamo clean_data, salvo il risultato in una variabile "words" e visualizzo le prime 100 parole del testo

    words = clean_data(data)
    print(words[:100])

    print("\n----------------------------------Most Common Words ordered by frequency-----------------------------------------\n")

    #chiamo mostCommon, salvo il risultato in una variabile "mc_30" e visualizzo come lista di tuple
    #(word, frequency) le 30 parole più frequenti nel testo in ordine decrescente di frequenza

    mc_30 = mostCommon(n=30, words=words)
    print(mc_30)



if __name__ == '__main__':
    main()
