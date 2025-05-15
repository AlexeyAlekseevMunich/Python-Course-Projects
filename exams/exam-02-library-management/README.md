# Exam 2: Basic Library Management System

## Task Description (General Overview)

The goal of this exam was to create a Python program for managing a simple library database. The program needed to provide the following functionalities:

1.  **Book Search:** A function to search for books by title or author.
2.  **Add Book:** A function to add a new book to the library database (represented as a list of dictionaries).
3.  **Filter Books by Year:** A function to return all books published in a specific year, utilizing the `filter()` function.
4.  **Display Database:** A function to display the current content of the library database.
5.  **Interactive Menu:** An interactive console menu allowing the user to access these functions, using a `while` loop for continuous operation.

## Solution Approach

The implemented solution (`library_manager.py`) addresses these requirements by:

*   **Data Structure:** Initializing and using a global list named `buecherei_datenbank` to store book data as dictionaries.
*   **Modular Functions:** Implementing each required functionality (`buecherei_anzeigen`, `buch_suchen`, `buecher_nach_jahr_filtern`, `buch_hinzufuegen`) as a separate Python function.
*   **Book Search Logic (`buch_suchen`):**
    *   Prompts the user for a search term.
    *   Iterates through the database, checking if the search term is present (as a substring) in either the book's "Titel" or "Autor".
    *   Collects and displays all matching books.
*   **Adding Books (`buch_hinzufuegen`):**
    *   Prompts the user for title, author, and publication year.
    *   Includes basic input validation for the year to ensure it's a digit.
    *   Creates a new dictionary for the book and appends it to the `buecherei_datenbank` list.
*   **Filtering by Year (`buecher_nach_jahr_filtern`):**
    *   Prompts the user for a year.
    *   Includes input validation for the year (must be digits).
    *   Uses `filter()` with a `lambda` function to efficiently select books where the "Jahr" matches the specified year.
    *   Displays the filtered list of books.
*   **Displaying Data (`buecherei_anzeigen`):**
    *   Iterates through the `buecherei_datenbank` and prints details of each book in a formatted way.
    *   Handles the case where the library is empty.
*   **Interactive Menu:**
    *   A `while True` loop presents a numbered menu of options to the user.
    *   User input (1-5) determines which function is called.
    *   Includes an option to exit the program and basic handling for invalid menu choices.

## Key Python Concepts Demonstrated:

*   **Functions:** Defining and calling functions to structure the program.
*   **Global Variables:** Using a global list (`buecherei_datenbank`) to store shared data (common in simpler scripts, though alternatives like passing data as arguments or using classes exist for larger applications).
*   **Data Structures:**
    *   **Lists:** Used as the main container for the library database.
    *   **Dictionaries:** Used to represent individual books with "Titel", "Autor", "Jahr" keys.
*   **Loops:**
    *   `for` loops for iterating through the list of books.
    *   `while` loop for the interactive menu and input validation (for year).
*   **Conditional Statements (`if/elif/else`):** For menu navigation and logic within functions.
*   **Built-in Functions:**
    *   `filter()`: Used with a `lambda` function for filtering.
    *   `input()`, `print()`, `int()`, `list()`.
*   **String Methods:** `isdigit()`, f-strings for formatted output.
*   **String Operators:** `in` operator for substring checking in `buch_suchen`.
*   **List Methods:** `append()` for adding books.
*   **Lambda Functions:** Used in conjunction with `filter()`.
*   **Input Validation:** Basic checks for numeric input for 'year'.
*   **Modularity & User Interaction:** Structuring the program into logical functions and providing a console-based menu.

## How to Run

1.  Save the code as `library_manager.py` in the `exams/exam-02-library-management/` directory.
2.  Open a terminal or command prompt.
3.  Navigate to the directory where you saved the file.
4.  Run the script using the command: `python library_manager.py`
5.  Follow the on-screen menu options.
