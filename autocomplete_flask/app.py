"""
File Name: app.py
Description: This file uses the Flask framework to implement a web application to provide word suggestions based on user input.
Author: Andrey Estevam Seabra
"""

from flask import Flask, render_template, request
import words_trie
from nltk.corpus import wordnet as wn

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def home_page():
    """
    This function renders the HTML code as well as accesses the suggestion of words based on user input.
    """
    suggestions_list = []
    if request.method == "POST":
        # Accesses the prefix and number of suggestions the user wants.
        prefix = request.form.get("prefix", "app") # Default prefix is "believe"
        try:
            num_suggestions = int(request.form.get("num_suggestions", 5)) # Default number of suggestions is 5.
            if num_suggestions <= 0:
                raise ValueError("The number of suggestions must be greater than zero.")
            # Accesses all the suggestions from the Trie and returns it 
            suggestions_list = [suggestion.capitalize() for suggestion in word_dictionary.give_suggestions(prefix)[:num_suggestions]]
        except ValueError:
            suggestions_list = ["The number of suggestions must be greater than zero."]
    
    return render_template("index.html", suggestions=suggestions_list)


# Loads the dictionary into a Trie data structure.
print("Loading the dictionary into the Trie... please wait :)")
words = set(wn.words("eng"))
word_dictionary = words_trie.TrieWords()
for word in words:
    word_dictionary.insert_word(word)
print("Successfully loaded!")

if __name__ == '__main__':
    app.run(debug=True)