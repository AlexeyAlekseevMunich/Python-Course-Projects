# Exam 1: Simple Console Calculator

## Task Description (General Overview)

The objective of this exam was to develop a console-based calculator program in Python. The program should:
1.  Prompt the user to select an arithmetic operation (Addition, Subtraction, Multiplication, Division).
2.  Ask the user for two numbers.
3.  Perform the selected operation with these numbers.
4.  Display the result.
5.  Implement error handling for invalid operator input and division by zero.
6.  Include comments in the code to explain the logic.
7.  Allow the user to perform multiple calculations until they choose to exit.

## Solution Approach

The implemented solution (`calculator.py`) achieves the required functionality as follows:

*   **User Interaction:** The program starts with a welcome message and enters a main `while` loop to allow for repeated calculations.
*   **Operation Selection:** The user is prompted to enter a letter (A, S, M, D) to choose an operation. Input validation ensures only valid letters are accepted.
*   **Number Input:** For the chosen operation, the user is asked to input two numbers.
    *   **Input Validation for Numbers:** A custom validation loop checks each character of the input string to ensure it's a digit, a minus sign ('-'), or a decimal point ('.'). This is done to prevent `ValueError` if `float()` is called on non-numeric input directly.
*   **Performing Calculation:** Based on the selected operation, the corresponding arithmetic is performed.
*   **Error Handling:**
    *   **Invalid Operator:** Handled by a `while` loop that re-prompts until a valid operator is entered.
    *   **Division by Zero:** Specifically checked before performing the division. The user is prompted to enter a different second number if they attempt to divide by zero.
    *   **Invalid Number Input:** Handled by the custom validation loop described above.
*   **Output:** The result of the calculation is displayed to the user using an f-string.
*   **Loop Continuation:** After each calculation, the user is asked if they want to perform another calculation. If not, the program exits.
*   **Comments:** The code includes comments explaining different sections and logic.

## Key Python Concepts Demonstrated:

*   **Input/Output:** Using `input()` to get user data and `print()` for displaying information.
*   **Data Types:** Working with strings (for input), floats (for calculations), and booleans (for control flow).
*   **Control Structures:**
    *   `if/elif/else` statements for conditional execution of operations.
    *   `while` loops for repeated calculations, input validation, and menu-driven interaction.
    *   `for` loops for iterating through input strings during number validation.
*   **String Operations:** Checking for membership in a list of allowed characters (`in ['A', 'S', 'M', 'D']`).
*   **Error Handling (Basic):** Implementing checks for invalid input and specific error conditions like division by zero.
*   **Type Conversion:** Using `float()` to convert string input to numbers.
*   **Code Comments:** Documenting the code for clarity.
*   **F-strings:** For formatted output.

## How to Run

1.  Ensure you have Python installed.
2.  Save the code as `calculator.py`.
3.  Open a terminal or command prompt.
4.  Navigate to the directory where you saved the file.
5.  Run the script using the command: `python calculator.py`
6.  Follow the on-screen prompts.
