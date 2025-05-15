# Exam 5: Tkinter Quiz Application with Timer and File I/O

## Task Description (General Overview)

The objective of this exam was to develop a Python GUI application using Tkinter for a simple quiz. The application should include:

1.  **Quiz Interface:** Display questions with multiple-choice answers presented as radio buttons.
2.  **Timer:** Implement a 30-second timer for each question, using threads to ensure the GUI remains responsive.
3.  **Navigation:** Buttons for starting the quiz, moving to the "Next Question," and saving/loading results.
4.  **Scoring:** Keep track of the user's score.
5.  **Results Storage:** Functions to save quiz results (score, questions, user answers, correct answers) to a text file and load them for display, using file dialogs for path selection.
6.  **Question Structure:** Questions stored as dictionaries including the question text, options, and the correct answer.

## Solution Approach

The implemented solution (`quiz_app.py`) creates a comprehensive quiz application with the following features:

*   **GUI with Tkinter:**
    *   A main window (`fenster`) hosts all widgets.
    *   Labels (`Label`) display welcome messages, questions, and the timer.
    *   Radio buttons (`Radiobutton`) allow users to select one answer from four options.
    *   Buttons (`Button`) for "Quiz starten", "Nächste Frage", "Ergebnisse speichern", and "Ergebnisse laden".
    *   A `Frame` is used to group buttons at the bottom.
    *   Dialogs (`filedialog.asksaveasfilename`, `filedialog.askopenfilename`) for saving and loading results.
    *   A `Toplevel` window is used to display loaded results.
*   **Quiz Logic:**
    *   A list of dictionaries (`questions`) stores the quiz content.
    *   Global variables manage the current question index (`current_question`), score (`score`), timer countdown (`countdown`), user answers (`user_answers`), and timer state (`running`, `counter_thread`, `stop_event`).
    *   The `start_quiz` function initializes/resets the quiz state and displays the first question.
    *   `next_question` loads the subsequent question, resets and restarts the timer.
    *   `check_answer` evaluates the selected answer, updates the score, records the user's answer, and proceeds to the next question or ends the quiz.
    *   `reset_quiz` is called at the end to return to the welcome screen.
*   **Timer Implementation:**
    *   A `countdown` variable tracks the remaining time.
    *   A `threading.Thread` (`counter_thread`) runs the `start_timer` function, which decrements `countdown` every second and updates the `timer_label`.
    *   A `threading.Event` (`stop_event`) is used to gracefully stop the timer thread when moving to the next question or if the quiz ends. This prevents multiple timers from running concurrently and ensures clean thread termination.
    *   The `start_new_timer` and `stop_timer` functions manage the lifecycle of the timer thread.
*   **Saving and Loading Results:**
    *   `save_results`: Prompts the user for a file path using `filedialog.asksaveasfilename`. Saves the overall score, each question, the user's answer for that question, and the correct answer to a `.txt` file.
    *   `load_results`: Prompts the user to select a previously saved results file using `filedialog.askopenfilename`. Reads the content and displays it in a new `Toplevel` window with a `Text` widget.
*   **User Experience:**
    *   Welcome screen before starting the quiz.
    *   Clear feedback on time-up and quiz completion via `messagebox.showinfo`.
    *   Buttons are enabled/disabled appropriately based on the quiz state.

## Key Python Concepts Demonstrated:

*   **GUI Programming (Tkinter):**
    *   Creating main windows (`Tk`), labels (`Label`), buttons (`Button`), radio buttons (`Radiobutton`), frames (`Frame`), and top-level windows (`Toplevel`).
    *   Using `StringVar` for radio button selections.
    *   Layout management with `pack()`.
    *   Event handling via `command` attribute of buttons.
    *   Using `tkinter.messagebox` for alerts and `tkinter.filedialog` for file operations.
*   **Threading (`threading` module):**
    *   Creating and managing daemon threads (`Thread`, `daemon=True`) for background tasks (timer) to keep the GUI responsive.
    *   Using `threading.Event` for inter-thread communication and graceful thread termination (`stop_event.set()`, `stop_event.clear()`, `stop_event.is_set()`).
    *   Using `thread.join()` to wait for a thread to complete.
*   **Time (`time` module):**
    *   Using `time.sleep()` within the timer thread.
*   **Data Structures:**
    *   Lists of dictionaries for storing quiz questions.
    *   Lists for storing user answers.
*   **Global Variables:** Managing quiz state (current question, score, timer status) across different functions.
*   **Functions:** Extensive use of functions to modularize different parts of the application (quiz logic, timer management, UI updates, file operations).
*   **File I/O:** Reading from and writing to text files (`open`, `with` statement, `read`, `write`) with `utf-8` encoding.
*   **Control Flow:** `if/else` statements, `for` loops.
*   **Error Handling (Implicit):** File dialogs handle cases where the user cancels, and `try-except` could be added for more robust file operations if needed (though not explicitly shown for basic file writing/reading in this snippet).

## How to Run

1.  Save the code as `quiz_app.py` in the `exams/exam-05-tkinter-quiz-app/` directory.
2.  Ensure you have Python and Tkinter installed (Tkinter is usually included with standard Python installations).
3.  Open a terminal or command prompt.
4.  Navigate to the directory where you saved the file.
5.  Run the script using the command: `python quiz_app.py`
6.  The Quiz Application window will appear. Interact with the buttons to play.
