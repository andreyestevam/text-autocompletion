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
        This method defines whether the sequence of characters, from root to current node, is a word or not.
        """
        return self.end_of_word

class TrieWords:
    def __init__(self) -> None:
        # Initializes the root of the data structure.
        self.root = CharactersTrieNode()
    
    def insert_word(self, word: str) -> None:
        """
        This method inserts a word to the Trie dictionary.
        """
        # If this is an empty str, there is no word to insert in the method. Otherwise, add the word to the dictionary.
        if not word:
            return
        cur_node = self.root
        for char in word.lower(): # Converts to lowercase.
            # Adds the character to the children's dictionary and iterates over the children's nodes until it gets to the end of the word.
            if char not in cur_node.children:
                cur_node.children[char] = CharactersTrieNode()
            cur_node = cur_node.children[char]
        
        # Flag this node to signalize this is a complete word.
        cur_node.end_of_word = True
    
    def prefix_search(self, prefix: str) -> CharactersTrieNode:
        """
        This method finds the location of the last character from the prefix, inputted by the user.
        With this information, we are able to find the words that can be suggested based on the location of the node of the last character in prefix.

        Return: the node locating the last character in the prefix.
        """
        cur_node = self.root
        # Starts the search for the last node holding the last letter of prefix, then returns it at the end.
        for letter in prefix:
            if letter not in cur_node.children:
                return None
            cur_node = cur_node.children[letter]
        return cur_node
    
    def give_suggestions(self, prefix: str) -> list:
        """
        Finds the prefix in the Trie data structure and returns up to num_suggestions words from the dictionary.
        """
        # Initializes variables, and checks if the current node is a word.
        cur_node = self.prefix_search(prefix.lower())
        if cur_node is None:
            return []
        
        words_list = []
        self._helper_give_suggestions(cur_node, prefix, words_list)
        return words_list
    
    def _helper_give_suggestions(self, cur_node: CharactersTrieNode, prefix: str, words_list: list) -> None:
        """
        Helper method of give_suggestions(). Collects all the words that begin with the prefix str.
        """
        # Base case (whenever the word is finished).
        if cur_node.is_word_finished():
            words_list.append(prefix)
        
        # Recursive case, which will iterate over all the items of the children of each node.
        for letter, child in cur_node.children.items():
            self._helper_give_suggestions(child, prefix + letter, words_list)