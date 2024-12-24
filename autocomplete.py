"""
File Name: setup.py
Description: This file uses the Trie data structure developed in words_trie to output the word autocomplete suggestions.
Author: Andrey Estevam Seabra
Usage: 
- Make sure to pip install nltk.
- Before running this file, make sure you have the dictionary installed (in this case, we are using the WordNet dataset). To download it, run
these following lines of code in your terminal:
    >>> import nltk
    >>> nltk.download('wordnet')
"""

from nltk.corpus import wordnet as wn

# Stores all the words from the dictionary in English.
word_list = set(wn.words("eng"))