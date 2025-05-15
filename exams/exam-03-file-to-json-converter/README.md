# Exam 3: Name List Processor (File I/O and JSON Conversion)

## Task Description (General Overview)

The objective of this exam was to develop a Python program with the following functionalities:

1.  **Read Names from File:** Implement a function to read a list of names from a specified text file (e.g., `namen.txt`), where each name is on a new line. This function should use the `with` statement and `try-except` blocks to handle potential file reading errors (like `FileNotFoundError`).
2.  **Save Names to JSON:** Create a function to convert the list of read names into JSON format and save it to a new file (e.g., `namen.json`). This function should also ensure proper file closure, even if errors occur during writing.
3.  **Console User Interface:** Implement a console-based menu to allow the user to choose between these functions or exit the program.
4.  **Direct Execution Guard:** Ensure the script's main logic (the menu) only runs when the script is executed directly (not when imported as a module).

## Solution Approach

The implemented solution (`name_processor.py`) addresses these requirements as follows:

*   **Global Name List:** A global list `namen` is used to store the names read from the file, making them accessible to both the reading and saving functions.
*   **Reading Names (`lese_namen`):**
    *   The function takes an optional filename argument (defaulting to `namen.txt`).
    *   It uses a `try-except` block to handle `FileNotFoundError` and other potential `Exception`s during file operations.
    *   The `with open(...)` statement ensures the file is properly closed.
    *   Each line (name) from the file is stripped of leading/trailing whitespace using `.strip()` and appended to the global `namen` list.
    *   Prints the loaded names or an error message.
*   **Saving Names to JSON (`speichere_namen`):**
    *   Checks if the `namen` list is populated; if not, it prompts the user to load names first by calling the `menue()` function (this could lead to nested menu calls, a simpler approach might be to just print a message and return).
    *   Uses `json.dumps(namen, indent=4)` to convert the list of names into a nicely formatted JSON string.
    *   Writes this JSON string to a specified file (e.g., `namen.json`) using `with open(...)` and a `try-except` block for error handling during saving.
*   **Interactive Menu (`menue`):**
    *   A `while True` loop presents a console menu with options to read names, save names as JSON, or exit.
    *   User input determines which function is called or if the program terminates.
*   **Direct Execution Guard:** The `if __name__ == "__main__":` block ensures that the `menue()` function is called only when the script is run directly.

## Key Python Concepts Demonstrated:

*   **File Handling:**
    *   Opening files in read (`'r'`) and write (`'w'`) modes.
    *   Using the `with open(...) as ...:` statement for automatic file closing.
    *   Iterating over lines in a file.
    *   Specifying `encoding='utf-8'` for broader character support.
*   **JSON Processing:**
    *   Importing the `json` module.
    *   Using `json.dumps()` to serialize a Python list into a JSON formatted string (with `indent=4` for pretty-printing).
    *   Writing JSON data to a file.
*   **Error Handling:**
    *   Using `try-except` blocks to catch specific exceptions like `FileNotFoundError` and general `Exception`s.
    *   Providing user-friendly error messages.
*   **Functions:** Defining functions for modularity (`lese_namen`, `speichere_namen`, `menue`).
*   **Global Variables:** Using a global list `namen` to share data between functions (with `global namen` keyword for modification).
*   **Data Structures:** Using lists to store names.
*   **String Methods:** `strip()` to remove whitespace.
*   **Conditional Execution:** `if __name__ == "__main__":` to control script execution.
*   **User Interaction:** Creating a console-based menu with `input()` and `print()`.
*   **Loops:** `while` loop for the menu and `for` loop for reading file lines.

## How to Run

1.  Save the code as `name_processor.py` in the `exams/exam-03-file-to-json-converter/` directory.
2.  (Optional but recommended for testing `lese_namen`) Create a text file named `namen.txt` in the same directory, with one name per line (e.g., Max Mustermann, Erika Musterfrau).
3.  Open a terminal or command prompt.
4.  Navigate to the directory where you saved the file(s).
5.  Run the script using the command: `python name_processor.py`
6.  Follow the on-screen menu options.
