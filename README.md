# text-autocompletion
This is an autocomplete system where users input a string, and possible completions are predicted based on a preloaded dataset.

## Program overview
- User types a word prefix.
- A list of suggestions that matches the input (prefix) is outputted.
- Stores and processes a large dataset of words (WordNet).
- Efficiently retrieves matching words based on the inputted prefix.

### Usage
- Make sure to pip install nltk.
- Before running the files main.py and app.py, make sure you have the dictionary installed (in this case, we are using the WordNet dataset). To download it, run these following lines of code in your terminal:
    ```python
    >>> import nltk
    >>> nltk.download('wordnet')
    ```

- Note: if you get an error called "CERTIFICATE_VERIFY_FAILED" when trying to run nltk.download('wordnet'), try to run this command in the terminal: /Applications/Python\ 3.x/Install\ Certificates.command (make sure to replace the x with the Python version installed in your computer).

### Citation
Dataset used in this application: Princeton University "About WordNet." WordNet. Princeton University. 2010. 