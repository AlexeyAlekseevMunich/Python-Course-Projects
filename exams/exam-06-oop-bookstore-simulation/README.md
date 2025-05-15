# Exam 6: Object-Oriented Bookstore Simulation with Tkinter GUI

## Task Description (General Overview)

The objective of this exam was to develop a Python program simulating a simple online bookstore using Object-Oriented Programming (OOP) principles and a Tkinter-based Graphical User Interface (GUI). The core requirements included:

1.  **Book Class:** Define a `Buch` class with attributes for title, author, category, and price, including `__init__` and `__str__` methods.
2.  **Bookstore Class:** Define a `Buchladen` class with an inventory (list of `Buch` objects) and methods for:
    *   Adding a book to the inventory.
    *   Searching the inventory by category.
    *   Calculating the total price of a selection of books.
3.  **GUI Implementation:** Create a Tkinter interface to interact with the bookstore functionalities.

## Solution Approach

The implemented solution (`bookstore_app.py`) creates a functional GUI application structured around three main classes: `Buch`, `Buchladen`, and `Program`.

*   **`Buch` Class:**
    *   Stores `titel`, `autor`, `kategorie`, and `preis` for each book.
    *   The `__str__` method provides a formatted string representation of a book, including the price formatted to two decimal places (e.g., "19.99 €").
*   **`Buchladen` Class:**
    *   Manages an `inventar` (list) of `Buch` objects.
    *   `buch_hinzufuegen(self, buch)`: Appends a `Buch` object to the inventory.
    *   `suchen_nach_kategorie(self, kategorie)`: Returns a list of books matching the given category (case-insensitive search).
    *   `gesamtpreis_berechnen(self, buecher)`: Calculates and returns the sum of prices for a given list of `Buch` objects.
*   **`Program` Class (GUI and Application Logic):**
    *   Initializes the main Tkinter window (`fenster`) and an instance of `Buchladen`.
    *   Manages a list `ausgewaehlte_buecher` for books selected by the user for purchase.
    *   **GUI Layout:** Uses `ttk.Frame` for structuring input fields and results. `grid()` layout manager is used for placing widgets.
        *   **Input Section:** `ttk.Entry` fields for title, author, category, and price. A button to add a new book. An entry field and button for searching by category.
        *   **Display Section:** A `tk.Listbox` (with `selectmode=tk.MULTIPLE`) to display all books or search results.
        *   **Action Buttons:** Buttons to "Alle Bücher anzeigen", "Auswahl anzeigen", "Zur Auswahl hinzufügen", "Aus der Auswahl löschen", and "Gesamtpreis der Auswahl".
    *   **Methods:**
        *   `hinzufuegen()`: Retrieves data from entry fields, creates a `Buch` object, adds it to the `Buchladen` inventory, shows a success message, and clears input fields. Includes `try-except` for `ValueError` if the price is not a valid float.
        *   `suchen()`: Clears the listbox and populates it with books matching the search category.
        *   `zeige_alle_buecher()`: Clears the listbox and displays all books from the inventory.
        *   `zeige_auswahl()`: Clears the listbox and displays books currently in the `ausgewaehlte_buecher` list.
        *   `zur_auswahl_hinzufuegen()`: Adds books selected in the listbox (from the main inventory display) to the `ausgewaehlte_buecher` list, avoiding duplicates.
        *   `aus_der_auswahl_loeschen()`: Removes books selected in the listbox (when viewing the current selection) from the `ausgewaehlte_buecher` list.
        *   `gesamtpreis_auswahl()`: Calculates and displays the total price of books in `ausgewaehlte_buecher` using `messagebox.showinfo`.
        *   `clear_entries()`: Clears all input fields.
*   **Main Execution:** The `if __name__ == "__main__":` block creates the Tkinter root window and an instance of the `Program` class, then starts the Tkinter event loop (`fenster.mainloop()`).

## Key Python Concepts Demonstrated:

*   **Object-Oriented Programming (OOP):**
    *   Defining classes (`Buch`, `Buchladen`, `Program`).
    *   Using `__init__` constructors to initialize object attributes.
    *   Implementing instance methods.
    *   Using the `__str__` special method for object representation.
    *   Encapsulation of data and behavior within classes.
*   **GUI Programming (Tkinter & `ttk`):**
    *   Using `tk.Tk` for the main window.
    *   Employing themed widgets from `tkinter.ttk` (`Frame`, `Label`, `Entry`, `Button`) for a more modern look.
    *   Using `tk.Listbox` with `selectmode=tk.MULTIPLE` for displaying and selecting multiple items.
    *   Layout management with `grid()`.
    *   Event handling with the `command` attribute of buttons.
    *   Using `tkinter.messagebox` (`showinfo`, `showerror`) for user feedback.
*   **Data Structures:** Lists for inventory and selected books.
*   **List Comprehensions:** Used in `suchen_nach_kategorie` and `aus_der_auswahl_loeschen` for concise list filtering.
*   **String Formatting:** F-strings, including formatting numbers to two decimal places (`.2f`).
*   **Error Handling:** `try-except ValueError` for price input validation.
*   **Modularity:** Separating data representation (`Buch`), business logic (`Buchladen`), and UI/application control (`Program`) into different classes.

## How to Run

1.  Save the code as `bookstore_app.py` in the `exams/exam-06-oop-bookstore-simulation/` directory.
2.  Ensure you have Python and Tkinter installed.
3.  Open a terminal or command prompt.
4.  Navigate to the directory where you saved the file.
5.  Run the script using the command: `python bookstore_app.py`
6.  The Bookstore Application window will appear. Use the input fields and buttons to manage and view books.
