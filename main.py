"""
File Name: main.py
Description: This file uses the Trie data structure developed in words_trie to output the word autocomplete suggestions.
Author: Andrey Estevam Seabra
"""

import autocomplete_flask.words_trie as words_trie
from nltk.corpus import wordnet as wn

def load_dictionary():
    """
    This function loads the WordNet dictionary into a Trie.
    Returns a Trie containing all the loaded words.
    """
    # Collects all the words from WordNet into a set and instantiates the Trie.
    print("Loading the dictionary into the Trie... please wait :)")
    words = set(wn.words("eng"))
    word_dictionary = words_trie.TrieWords()

    # Iterates over the Trie inserting all the words in the set.
    for word in words:
        word_dictionary.insert_word(word)
    print("Successfully loaded!")
    return word_dictionary

if __name__ == '__main__':
    
    # Starts by loading the Trie data structure with all the words from WordNet.
    word_dictionary = load_dictionary()

    while True:
        # Asks user for the prefix and how many suggestions they want.
        prefix = str(input("\nType an incomplete word and we will give you suggestions (type 'exit' to quit the program): "))
        if prefix.lower() == 'exit':
            print("Exiting the program. Thank you for using it!")
            break

        # Asks user for the number of suggestions
        try:
            num_suggestions = int(input("How many suggestions do you want? "))
            if num_suggestions <= 0:
                print("Please enter a positive number for the suggestions.")
                continue
        except ValueError:
            print("Invalid value. Please enter a valid number for suggestions.")
            continue

        # Finds the words in the Trie that have the inputted prefix.
        words_list = word_dictionary.give_suggestions(prefix)

        if not words_list:
            print("No suggestions found.")
        else:
            print("\nSuggestions:")
            for word in words_list[:num_suggestions]:
                print("- " + word.capitalize())