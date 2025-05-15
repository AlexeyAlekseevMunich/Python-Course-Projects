# Project: Extractive Text Summarizer

This project implements a basic extractive text summarization algorithm in Python using the Natural Language Toolkit (NLTK). The goal was to independently research and apply text processing techniques to select the most important sentences from a given text to form a summary.

## Project Objective

The program performs the following steps to generate a summary:
1.  **Tokenize the Text:** Break down the input text into individual sentences and words.
2.  **Clean the Text:**
    *   Remove punctuation marks.
    *   Remove common stop words (e.g., "the", "is", "in").
3.  **Calculate Word Frequencies:** Count the occurrences of each remaining (cleaned) word in the text.
4.  **Score Sentences:**
    *   For each original sentence, calculate a score. The score is the sum of the frequencies of the (cleaned) words it contains.
5.  **Select Top Sentences:** Choose the top 20% of sentences with the highest scores to form the summary.

## Solution Approach

The solution is structured using a `TextAnalyzer` class to encapsulate text processing functionalities and a separate function `summarize_text` to generate the final summary.

*   **`TextAnalyzer` Class:**
    *   **Initialization (`__init__`):** Loads English stop words from NLTK and a set of punctuation characters from the `string` module.
    *   **`tokenize_text(self, text)`:** Uses `nltk.tokenize.sent_tokenize` for sentence tokenization and `nltk.tokenize.word_tokenize` for word tokenization.
    *   **`remove_punctuation(self, words)`:** Filters out words that are purely punctuation.
    *   **`remove_stopwords(self, words)`:** Filters out common English stop words (case-insensitive).
    *   **`preprocess_text(self, text)`:** A pipeline method that tokenizes the text, then removes punctuation and stop words from the tokenized words. It returns the original sentences, words with punctuation removed, and fully cleaned words.
    *   **`count_word_frequencies(self, words)`:** Uses `collections.defaultdict(int)` to count the frequency of each word in the provided list of cleaned words.
    *   **`calculate_sentence_counts(self, sentences, word_counts)`:** For each original sentence:
        1.  It re-tokenizes the sentence into words and removes punctuation (to match the words used for frequency counting).
        2.  It sums the frequencies (from `word_counts`) of these words to get the sentence's score.
        3.  Stores sentence-score pairs in a dictionary.
*   **`summarize_text(sentence_counts)` Function:**
    *   Takes the dictionary of sentences and their scores.
    *   Sorts the sentences in descending order based on their scores.
    *   Calculates 20% of the total number of sentences (ensuring at least 1 sentence is selected).
    *   Selects the top N sentences from the sorted list.
    *   Joins these selected sentences into a single string to form the summary.
*   **Main Execution Block (`if __name__ == "__main__":`)**:
    *   Provides an example input text.
    *   Instantiates `TextAnalyzer`.
    *   Calls the methods in sequence: preprocess, count word frequencies, calculate sentence scores.
    *   Calls `summarize_text` to get the final summary.
    *   Prints the summary to the console.
*   **NLTK Resource Downloads:** The script includes `nltk.download('punkt')` and `nltk.download('stopwords')` to ensure the necessary NLTK resources are available.

## Key Python & NLP Concepts Demonstrated:

*   **Natural Language Processing (NLP) with NLTK:**
    *   Sentence Tokenization (`nltk.tokenize.sent_tokenize`).
    *   Word Tokenization (`nltk.tokenize.word_tokenize`).
    *   Stop Word Removal (`nltk.corpus.stopwords`).
*   **Text Preprocessing:** Common NLP steps like removing punctuation and stop words.
*   **Frequency Analysis:** Calculating word frequencies using `collections.defaultdict`.
*   **Extractive Summarization Algorithm:** Implementing a basic scoring mechanism for sentences based on word frequencies.
*   **Object-Oriented Programming (OOP):** Using a class (`TextAnalyzer`) to organize related text processing functions and manage state (stop words, punctuation).
*   **Data Structures:**
    *   Lists for storing sentences, words.
    *   Sets for efficient lookup of stop words and punctuation.
    *   Dictionaries for word frequencies and sentence scores.
*   **Functions & Modularity:** Breaking down the problem into smaller, manageable functions/methods.
*   **Lambda Functions:** Used as the `key` for sorting sentences by score (`key=lambda x: x[1]`).
*   **Standard Library Modules:** `string`, `collections`.
*   **Problem Solving & Independent Research:** The project required understanding and implementing an NLP task based on a set of general steps.

## How to Run

1.  Save the code as `text_summarizer.py` (or similar) in the `project/extractive-text-summarizer/` directory.
2.  Ensure you have Python and the NLTK library installed. If not, install NLTK:
    ```bash
    pip install nltk
    ```
3.  Run the script from your terminal:
    ```bash
    python text_summarizer.py
    ```
4.  The script will download necessary NLTK resources (`punkt` tokenizer models and `stopwords` corpus) if they are not already present.
5.  It will then process the example text embedded in the script and print the generated summary to the console.

## Potential Enhancements (Future Work)

*   Allowing text input from a file or user input instead of a hardcoded string.
*   Supporting other languages for stop words.
*   Implementing more sophisticated sentence scoring (e.g., TF-IDF, positional importance).
*   Using stemming or lemmatization for better word normalization before frequency counting.
*   More advanced handling of punctuation within words (e.g., "U.S.A.").
