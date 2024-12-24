"""
File Name: words_trie.py
Description: This file implements the Trie (Prefix Tree) data structure to work with all the dictionary dataset.
Author: Andrey Estevam Seabra
"""

class CharactersTrieNode:
    """
    This class contains the node for each character of a certain word.
    """
    def __init__(self) -> None:
        # Initializes both children and flags if this is the end of the word.
        self.children = {}
        self.end_of_word = False
    
    def is_word_finished(self) -> bool:
        """
        This method defines whether the sequence of characters, from root to
        current node, is a word or not (determined if there exists a key '*' in the dictionary).
        """
        if('*' in self.children):
            self.end_of_word = True
        else:
            self.end_of_word = False
        return self.end_of_word

class TrieWords:
    def __init__(self) -> None:
        # Initializes the root of the data structure.
        self.root = CharactersTrieNode()
    
    def insert_word(self, word: str) -> None:
        """
        This method inserts all the words of the WordNet dictionary in the Trie.
        """