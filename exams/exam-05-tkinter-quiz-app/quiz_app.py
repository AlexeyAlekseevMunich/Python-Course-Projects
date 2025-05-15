# Teilprüfung 5
# Quiz mit Fragen (mit Tkinter)
# Radiobuttons mit Fragen und mehreren Antwortmöglichkeiten (Fragen/Antworten selbst ausdenken)
# Threads für Timer
# Butten für Starten(nicht in Anforderung), Nachste Frage, Ergebnisse speichern, Ergebnisse laden
# Funktionen für Ergebnisse speichern, Ergebnisse laden


# Import von Modulen
from tkinter import *  # Führt zu "Problems" aber ist funktionsfähig. Kann auch einzenl importiert werden, dann keine "Problems"
from tkinter import messagebox, filedialog
import threading
import time

# Globale Variablen setzen
current_question = 0  # Aktuelle Frage-Nummer in der Fragenliste  
score = 0  # Anzahl der richtig beantworteten Fragen  
running = False  # Status-Flag, ob der Timer läuft  
counter_thread = None  # Variable für den Timer-Thread  
countdown = 30  # Zeitlimit pro Frage in Sekunden  
user_answers = []  # Liste der Benutzerantworten zur späteren Speicherung  

# Fragen in einer Liste von Dictionaries
questions = [
    {
        "question": "Wie viele Beine hat ein Hund?",
        "options": ["2", "4", "6", "8"],
        "answer": "4"
    },
    {
        "question": "Welches Tier macht 'Miau'?",
        "options": ["Hund", "Katze", "Kuh", "Pferd"],
        "answer": "Katze"
    },
    {
        "question": "Was wächst auf Bäumen?",
        "options": ["Äpfel", "Fische", "Autos", "Schuhe"],
        "answer": "Äpfel"
    },
    {
        "question": "Wie viele Monate hat ein Jahr?",
        "options": ["10", "12", "24", "6"],
        "answer": "12"
    },
    {
        "question": "Was ist der kleinste Planet in unserem Sonnensystem?",
        "options": ["Erde", "Mars", "Merkur", "Venus"],
        "answer": "Merkur"
    }
]
#------------------------------------------------------------------------------------------------------------------------------------------
# Timer-Funktionen 
# (Wahrscheinlich nicht die beste und zu komplizierte Lösung. Anderes nicht geschafft, damit nicht mehrere Timer gleichzeitig laufen)
stop_event = threading.Event()  # Timer als Threading-Event

def start_new_timer():
    global countdown, running, counter_thread
    running = True  # Mit True Timer starten
    stop_event.clear()  # Stop-Event leeren, um den Timer fortzusetzen

    def start_timer(label):  # Timer starten
        global countdown, running
        while countdown > 0 and running and not stop_event.is_set():  # Während Timer läuft
            label.config(text=f"Restzeit: {countdown} Sekunden")  # Verbleibende Zeit
            time.sleep(1)
            countdown -= 1

        if running and not stop_event.is_set():  # Wenn der Timer zu Ende ist und nicht gestoppt wurde
            label.config(text="Zeit abgelaufen!")  # Zeit ist abgelaufen
            next_question_button.config(state="disabled")  # Button "Nächste Frage" deaktivieren
            start_button.config(state="normal")  # Button "Quiz starten" aktivieren

    counter_thread = threading.Thread(target=start_timer, args=(timer_label,))  # Timer in neuem Thread
    counter_thread.daemon = True  # Thread als Daemon-Thread
    counter_thread.start()  # Timer-Thread starten

#-------------------------------------------------------------------------------------------------------------------------------------------
def stop_timer():
    global running
    running = False  # Timer stoppen
    stop_event.set()  # Stop-Event, um den Timer zu stoppen
    if counter_thread is not None and counter_thread.is_alive():  # Wenn Timer-Thread läuft
        counter_thread.join()  # Wartet bis Timer-Thread endet
    next_question_button.config(state="disabled")
    start_button.config(state="normal")

#------------------------------------------------------------------------------------------------------------------------------------------
def next_question():
    global current_question, countdown, running, score
    if current_question < len(questions):  # Wenn noch Fragen vorhanden sind
        question = questions[current_question]  # Aktuelle Frage
        question_label.config(text=question["question"])  # Zu Label
        for i, option in enumerate(question["options"]):
            answer_buttons[i].config(text=option, value=option)  # Aktualisiert die Textbeschriftung der Antwort-Buttons

        selected_answer.set(None)  # Auswahl der Antwort zurücksetzen
        countdown = 30  # Timer auf 30 Sekunden
        if counter_thread is not None and counter_thread.is_alive():
            stop_timer()  # Timer stoppen
        start_new_timer()  # Neuen Timer starten
        next_question_button.config(state="normal")  # Nächste Frage
    else:  # Keine übrige Fragen
        messagebox.showinfo("Quiz beendet", f"Quiz abgeschlossen! Du hast {score} von {len(questions)} Fragen richtig beantwortet.")
        stop_timer()
        reset_quiz()

#-------------------------------------------------------------------------------------------------------------------------------------------
def reset_quiz():
    global score, current_question, countdown, user_answers
    score = 0  # Punktestand zurücksetzen
    current_question = 0  # Wieder erste Frage
    countdown = 30  # Timer auf 30 zurücksetzen
    user_answers = []  # Die Liste leeren
    start_button.config(state="normal")  # Button "Quiz starten" wieder aktivieren
    welcome_label.pack(pady=20) # Willkommenslabel 
    for button in answer_buttons: #Verstecken 
        button.pack_forget()
    question_label.pack_forget()
    timer_label.pack_forget()

#----------------------------------------------------------------------------------------------------------------------------------------
def check_answer():
    global current_question, score
    user_answer = selected_answer.get()  # Ausgewählte Antwort abrufen

    if user_answer:
        user_answers.append(user_answer)  # Antwort zur Liste
        if user_answer == questions[current_question]["answer"]:
            score += 1  # Punktestand
        current_question += 1  # Zur nächsten Frage
        if current_question < len(questions):  # Weiter nur wenn noch Fragen übrig
            next_question()
        else:
            next_question_button.config(state="disabled")  # Button "Nächste Frage" deaktivieren
            messagebox.showinfo("Quiz beendet", f"Quiz abgeschlossen! Du hast {score} von {len(questions)} Fragen richtig beantwortet.")

#--------------------------------------------------------------------------------------------------------------------------------------------
def save_results():
    global score  # Dialog zum Speichern der Datei (.txt)
    file_path = filedialog.asksaveasfilename(defaultextension=".txt", filetypes=[("Textdateien", "*.txt")])
    if file_path:
        with open(file_path, "w", encoding="utf-8") as file:  # Ergebnisse in die Datei
            file.write(f"Quiz-Ergebnisse:\n\nDu hast {score} von {len(questions)} Fragen richtig beantwortet.\n\n")
            for i, question in enumerate(questions):  # Speichern die Frage, die Antwort des Benutzers und die richtige Antwort
                user_answer = user_answers[i] if i < len(user_answers) else "Keine Antwort gewählt"
                file.write(f"Frage {i+1}: {question['question']}\n")  # Frage
                file.write(f"Deine Antwort: {user_answer}\n")  # Antwort
                file.write(f"Richtige Antwort: {question['answer']}\n\n")  # Richtige Antwort
        messagebox.showinfo("Ergebnisse gespeichert", "Deine Ergebnisse wurden gespeichert!")  # Nachricht: Ergebnisse gespeichert

#-------------------------------------------------------------------------------------------------------------------------------------------
def load_results():  # Textdatei laden
    file_path = filedialog.askopenfilename(filetypes=[("Textdateien", "*.txt")])
    if file_path: 
        with open(file_path, "r", encoding="utf-8") as file:
            data = file.read()
        result_window = Toplevel(fenster)  # Neues Fenster mit Ergebnissen
        result_window.title("Geladene Ergebnisse") 
        result_text = Text(result_window, wrap="word", font=("Arial", 12))   # Textfeld
        result_text.insert("1.0", data)  # Daten einfühgen
        result_text.config(state="disabled")  # Blockieren
        result_text.pack(expand=True, fill="both", padx=10, pady=10)  # Text platzieren

#--------------------------------------------------------------------------------------------------------------------------------------------
def start_quiz():
    global current_question, score, user_answers
    score = 0  # Punktestand zurück
    current_question = 0  # Aktuelle Frage ->erste Frage
    user_answers = []  # NeustartL-> Liste leeren
    start_button.config(state="disabled")  # Button "Quiz starten" deaktivieren
    welcome_label.pack_forget()
    question_label.pack(pady=20)  # Fragenlabel
    for button in answer_buttons:
        button.pack(anchor="w", padx=100)
    timer_label.pack(pady=10)
    next_question()

#----------------------------------------------------------------------------------------------------------------------------------------
fenster = Tk()  # Fenster erstellen
fenster.title("Quiz App")
fenster.geometry("500x350")
fenster.resizable(False, False)  # Blockieren Größe

welcome_label = Label(fenster, text="Willkommen zum Quiz-Spiel! \nDrücke auf 'Starten', um zu beginnen!", font=("Arial", 18))  # Willkommens-Label
welcome_label.pack(pady=20)

question_label = Label(fenster, text="", font=("Arial", 16), wraplength=400)  # Frage-Label

selected_answer = StringVar()  # Antwort-Radiobuttons
answer_buttons = []
for i in range(4):  # Vier Antwortmöglichkeiten
    button = Radiobutton(fenster, text="", variable=selected_answer, value="", font=("Arial", 14))
    answer_buttons.append(button)

timer_label = Label(fenster, text="Restzeit: 30 Sekunden", font=("Arial", 14))   # Timer-Label

button_frame = Frame(fenster) # Frame für die Buttons am unteren Rand
button_frame.pack(side="bottom", pady=10)

start_button = Button(button_frame, text="Quiz starten", font=("Arial", 10), command=start_quiz) 
start_button.pack(side="left", padx=9)

next_question_button = Button(button_frame, text="Nächste Frage", font=("Arial", 10), command=check_answer)
next_question_button.pack(side="left", padx=9)

save_button = Button(button_frame, text="Ergebnisse speichern", font=("Arial", 10), command=save_results)
save_button.pack(side="left", padx=9)

load_button = Button(button_frame, text="Ergebnisse laden", font=("Arial", 10), command=load_results)
load_button.pack(side="left", padx=9)


fenster.mainloop()
#--------------------------------------------------------------------------------------------------------------------------------------------------------------
