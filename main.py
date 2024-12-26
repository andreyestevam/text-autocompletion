"""
File Name: main.py
Description: This file uses the Trie data structure developed in words_trie to output the word autocomplete suggestions.
Author: Andrey Estevam Seabra
Usage: 
- Make sure to pip install nltk.
- Before running this file, make sure you have the dictionary installed (in this case, we are using the WordNet dataset). To download it, run
these following lines of code in your terminal:
    >>> import nltk
    >>> nltk.download('wordnet')

- Note: if you get an error "CERTIFICATE_VERIFY_FAILED" when trying to run nltk.download('wordnet'), try to run this command in the
terminal: /Applications/Python\ 3.x/Install\ Certificates.command (make sure to replace the x with your Python version).
"""

import words_trie
from nltk.corpus import wordnet as wn

if __name__ == '__main__':
    # Stores all the words from the dictionary in English.
    words = set(wn.words("eng"))
    word_dictionary = words_trie.TrieWords()
    for word in words:
        word_dictionary.insert_word(word)
    prefix = str(input("Type an incomplete word and we will give you suggestions: "))
    words_list = word_dictionary.give_suggestions(prefix)
    print("Suggestions: " + words_list)