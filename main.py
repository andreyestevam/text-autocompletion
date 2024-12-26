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
    # Loads the dictionary into a Trie data structure.
    print("Loading the dictionary into the Trie... please wait :)")
    words = set(wn.words("eng"))
    word_dictionary = words_trie.TrieWords()
    for word in words:
        word_dictionary.insert_word(word)
    print("Successfully loaded!")

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