# Exam 4: Customer Feedback Analysis Tool

## Task Description (General Overview)

The objective of this exam was to develop a Python program to analyze a text file (`feedback.txt`) containing customer feedback. The program should:

1.  **Read Feedback File:** Read the content of `feedback.txt`, ensuring proper file closure and handling potential I/O errors. (The task implied skipping a header line if present).
2.  **Extract Dates:** Use regular expressions to extract all dates in `DD.MM.YYYY` format from the feedback text.
3.  **Count Date Occurrences:** Count how often each extracted date appears and store the results in a dictionary.
4.  **Identify "Excellent" Comments:** Find all comments containing the word "exzellent" (case-insensitive).
5.  **Save Results to JSON:** Store the dictionary of date occurrences and the list of "excellent" comments in two separate JSON files (`datums_vorkommen.json` and `exzellente_feedbacks.json`).
6.  **Error Handling:** Implement `try-except` blocks for robust error handling during file operations and data processing.
7.  **Unicode Output:** (Optional) Use Unicode characters (emojis) in console output to signal success or issues.
8.  **(Implied)** Create a sample `feedback.txt` for testing.

## Solution Approach

The implemented solution (`feedback_analyzer.py`) performs these tasks sequentially:

*   **Import necessary modules:** `re` for regular expressions and `json` for JSON handling.
*   **Reading Feedback (`lese_feedback`):**
    *   Opens the specified file (default `feedback.txt`) with `utf-8` encoding.
    *   Includes a `next(file)` to skip a potential header line (as implemented).
    *   Reads each line, strips whitespace, and appends it to a list.
    *   Handles `FileNotFoundError` and general `Exception`s, returning `None` on error.
    *   Uses emojis in print statements for user feedback.
*   **Extracting Dates (`extrahiere_datumsangaben`):**
    *   Takes the list of feedback lines as input.
    *   Uses `re.findall(r"\b\d{2}\.\d{2}\.\d{4}\b", line)` to find all occurrences of dates in the specified format within each line.
    *   Collects all found dates into a list.
    *   Handles potential exceptions during extraction.
*   **Counting Dates (`zaehle_datumsangaben`):**
    *   Takes the list of extracted dates.
    *   Iterates through the list, using a dictionary to store the count of each unique date.
    *   Handles potential exceptions.
*   **Finding "Excellent" Comments (`finde_exzellente_kommentare`):**
    *   Iterates through the feedback list.
    *   For each comment, it converts the comment to lowercase (`kommentar.lower()`) and uses `re.findall(r"\bexzellent\b", ...)` to find occurrences of the word "exzellent" (as a whole word, case-insensitively).
    *   Appends matching original comments to a list.
    *   Handles potential exceptions.
*   **Saving Data to JSON (`speichere_daten_in_json`):**
    *   A generic function that takes a filename and data (dictionary or list).
    *   Uses `json.dump(daten, json_file, indent=4)` to write the data to the specified JSON file in a readable format.
    *   Handles potential exceptions during file writing.
*   **Main Execution Block:**
    *   The script calls these functions in sequence.
    *   It first reads the feedback. If successful, it proceeds to extract dates, count them, find excellent comments, and finally saves the results to the respective JSON files.
    *   Intermediate results (extracted dates, counts, excellent comments) are printed to the console for verification.

## Key Python Concepts Demonstrated:

*   **File Handling:** Reading from text files (`with open(...)`), specifying `utf-8` encoding, handling `FileNotFoundError`.
*   **Regular Expressions (`re` module):**
    *   Defining regex patterns (e.g., `r"\b\d{2}\.\d{2}\.\d{4}\b"` for dates, `r"\bexzellent\b"` for whole word matching).
    *   Using `re.findall()` to extract all matching patterns from text.
*   **JSON Processing (`json` module):**
    *   Using `json.dump()` to serialize Python objects (dictionaries, lists) into JSON files with pretty-printing (`indent=4`).
*   **Data Structures:**
    *   **Lists:** For storing feedback lines, extracted dates, and excellent comments.
    *   **Dictionaries:** For storing the frequency count of dates.
*   **Error Handling:** Comprehensive use of `try-except` blocks for `FileNotFoundError` and general `Exception`s in each function.
*   **String Methods:** `strip()`, `lower()`.
*   **Functions:** Well-defined functions for each distinct task, promoting modularity and reusability.
*   **Loops:** `for` loops for iterating through lines, lists, and dictionary items.
*   **Conditional Logic:** `if` statements to check for empty lists or successful file reads before proceeding.
*   **Unicode Characters:** Using Unicode escape sequences (e.g., `\U0001F6D1`) for emojis in console output.

## How to Run

1.  Save the code as `feedback_analyzer.py` in the `exams/exam-04-feedback-analyzer/` directory.
2.  Create a text file named `feedback.txt` in the same directory. Populate it with sample customer feedback, including some dates in `DD.MM.YYYY` format and some instances of the word "exzellent" (in various cases).
    *Example `feedback.txt` content:*
    ```
    Header Line To Be Skipped
    The service on 10.03.2023 was exzellent!
    I had an issue on 15.04.2023, but it was resolved.
    Excellent support.
    Another comment from 10.03.2023.
    ```
3.  Open a terminal or command prompt.
4.  Navigate to the directory where you saved the file(s).
5.  Run the script using the command: `python feedback_analyzer.py`
6.  The script will print intermediate results to the console and create/update `datums_vorkommen.json` and `exzellente_feedbacks.json` in the same directory.
