# Teilprüfung_06
# GUI - Online-Buchladen mit Funktonen: Buch hinzufügen, Buch suchen nach Kategorie, Gesamtpreis für eine Auswahl berechnen.
# Nicht in Anforderungen zusätzliche Funktionen: Alle  Bücher in Buchladen anzeigen, Zu Auswahl hinzufügen/löchen, Auswahl anzeigen. 
# (War nicht ganz klar: "das Berechnen des Gesamtpreises einer Buchauswahl")
# Buch mit Titel, Autor, Kategorie, Preis
# Oberfläche mit tkinter


import tkinter as tk  # Tkinter import
from tkinter import ttk, messagebox  # Import von Messagebox

#--------------------------------------------------------------------------------------------------------------------------------
class Buch:  # Class Buch mit Titel, Autor, Kategorie und Preis
    def __init__(self, titel, autor, kategorie, preis):
        self.titel = titel
        self.autor = autor
        self.kategorie = kategorie
        self.preis = preis

    def __str__(self):  # Zeichenkette für das Buch
        return f"{self.titel} von {self.autor} ({self.kategorie}) - {self.preis:.2f} €"  # mit zwei Nachkommastellen (19.99 €)

#--------------------------------------------------------------------------------------------------------------------------------
class Buchladen:
    def __init__(self):
        self.inventar = [] # Class Buchladen mit einem leeren Inventar

    def buch_hinzufuegen(self, buch):  # Buch hinzufügen
        self.inventar.append(buch)

    def suchen_nach_kategorie(self, kategorie):  # Büchern nach einer Kategorie suchen
        return [buch for buch in self.inventar if buch.kategorie.lower() == kategorie.lower()]

    def gesamtpreis_berechnen(self, buecher):  # Gesamtkosten für Büchern in der Liste
        return sum(buch.preis for buch in buecher)

#---------------------------------------------------------------------------------------------------------------------------------
class Program:    # Hauptprogramm und GUI
    def __init__(self, fenster):
        self.verwaltung = Buchladen()  # Buchladen-Instanz
        self.ausgewaehlte_buecher = []
        self.fenster = fenster
        self.fenster.title("Buchladen " + chr(0x1F4D6))

        self.eingabe_frame = ttk.Frame(self.fenster)  # Eingabe-Frame
        self.eingabe_frame.grid(row=0, column=0, padx=10, pady=10)

        ttk.Label(self.eingabe_frame, text="Titel:").grid(row=0, column=0)  # Eingabefeld und Label
        self.name_entry = ttk.Entry(self.eingabe_frame)
        self.name_entry.grid(row=0, column=1)

        ttk.Label(self.eingabe_frame, text="Autor:").grid(row=1, column=0)
        self.autor_entry = ttk.Entry(self.eingabe_frame)
        self.autor_entry.grid(row=1, column=1)

        ttk.Label(self.eingabe_frame, text="Kategorie:").grid(row=2, column=0)
        self.kategorie_entry = ttk.Entry(self.eingabe_frame)
        self.kategorie_entry.grid(row=2, column=1)

        ttk.Label(self.eingabe_frame, text="Preis:").grid(row=3, column=0)
        self.preis_entry = ttk.Entry(self.eingabe_frame)
        self.preis_entry.grid(row=3, column=1)

        ttk.Button(self.eingabe_frame, text="Buch hinzufügen", command=self.hinzufuegen).grid(row=4, column=0, columnspan=2, pady=5)  # Button

        ttk.Label(self.eingabe_frame, text="Suchen nach Kategorie:").grid(row=5, column=0)  # Suchfunktion für Bücher
        self.suchen_entry = ttk.Entry(self.eingabe_frame)
        self.suchen_entry.grid(row=5, column=1)
        ttk.Button(self.eingabe_frame, text="Suchen", command=self.suchen).grid(row=6, column=0, columnspan=2, pady=5)
        
        ttk.Button(self.eingabe_frame, text="Alle Bücher anzeigen", command=self.zeige_alle_buecher).grid(row=7, column=0, columnspan=2, pady=5) # Button
        ttk.Button(self.eingabe_frame, text="Auswahl anzeigen", command=self.zeige_auswahl).grid(row=8, column=0, columnspan=2, pady=5)

        self.ergebnis_frame = ttk.Frame(self.fenster)  # Ergebnis-Frame
        self.ergebnis_frame.grid(row=1, column=0, padx=10, pady=10)

        self.listbox = tk.Listbox(self.ergebnis_frame, height=10, width=50, selectmode=tk.MULTIPLE)  # Listbox für die Buchanzeige
        self.listbox.grid(row=0, column=0)

        button_frame = ttk.Frame(self.ergebnis_frame)  # Button für Auswahloptionen
        button_frame.grid(row=1, column=0, pady=5)

        ttk.Button(button_frame, text="Zur Auswahl hinzufügen", command=self.zur_auswahl_hinzufuegen).grid(row=0, column=0, padx=5)  # Buttons zur Auswahl
        ttk.Button(button_frame, text="Aus der Auswahl löschen", command=self.aus_der_auswahl_loeschen).grid(row=0, column=1, padx=5)
        
        ttk.Button(self.ergebnis_frame, text="Gesamtpreis der Auswahl", command=self.gesamtpreis_auswahl).grid(row=2, column=0, pady=5)  # Button

#-----------------------------------------------------------------------------------------------
    def hinzufuegen(self): # Buch zur Bibliothek hinzufügen
        titel = self.name_entry.get()
        autor = self.autor_entry.get()
        kategorie = self.kategorie_entry.get()
        preis_text = self.preis_entry.get()
        try:
            preis = float(preis_text)
            buch = Buch(titel, autor, kategorie, preis)
            self.verwaltung.buch_hinzufuegen(buch)
            messagebox.showinfo("Erfolg", "Buch wurde hinzugefügt!")
            self.clear_entries()
        except ValueError:
            messagebox.showerror("Fehler", "Bitte den Preis mit Punkt eingeben, z. B. 19.99")

#-----------------------------------------------------------------------------------------------
    def suchen(self):  # Nach bestimmte Kategorie urchsuchen
        self.listbox.delete(0, tk.END)
        kategorie = self.suchen_entry.get()
        ergebnisse = self.verwaltung.suchen_nach_kategorie(kategorie)
        for buch in ergebnisse:
            self.listbox.insert(tk.END, str(buch))
    
#-----------------------------------------------------------------------------------------------    
    def zeige_alle_buecher(self): # Alle Bücher im Inventar
        self.listbox.delete(0, tk.END)
        for buch in self.verwaltung.inventar:
            self.listbox.insert(tk.END, str(buch))

#-----------------------------------------------------------------------------------------------    
    def zeige_auswahl(self):  # Nur ausgewählte Bücher
        self.listbox.delete(0, tk.END)
        for buch in self.ausgewaehlte_buecher:
            self.listbox.insert(tk.END, str(buch))

#-----------------------------------------------------------------------------------------------
    def zur_auswahl_hinzufuegen(self): # Ausgewählte Bücher zu Auswahl
        ausgewählte_indices = self.listbox.curselection()
        for index in ausgewählte_indices:
            buch_text = self.listbox.get(index)
            for buch in self.verwaltung.inventar:
                if str(buch) == buch_text and buch not in self.ausgewaehlte_buecher:
                    self.ausgewaehlte_buecher.append(buch)
        messagebox.showinfo("Erfolg", "Bücher zur Auswahl hinzugefügt!")

#-----------------------------------------------------------------------------------------------
    def aus_der_auswahl_loeschen(self): # Ausgewählte Bücher aus Auswahl
        ausgewählte_indices = self.listbox.curselection()
        for index in reversed(ausgewählte_indices):
            buch_text = self.listbox.get(index)
            self.ausgewaehlte_buecher = [buch for buch in self.ausgewaehlte_buecher if str(buch) != buch_text]
        self.zeige_auswahl()

#-----------------------------------------------------------------------------------------------
    def gesamtpreis_auswahl(self): # Gesamtpreis der ausgewählten Bücher 
        gesamtpreis = self.verwaltung.gesamtpreis_berechnen(self.ausgewaehlte_buecher)
        messagebox.showinfo("Gesamtpreis", f"Der Gesamtpreis der Auswahl beträgt: {gesamtpreis:.2f} €")

#-----------------------------------------------------------------------------------------------
    def clear_entries(self): #Eingabefelder löschen
        self.name_entry.delete(0, tk.END)
        self.autor_entry.delete(0, tk.END)
        self.kategorie_entry.delete(0, tk.END)
        self.preis_entry.delete(0, tk.END)
        self.suchen_entry.delete(0, tk.END)

#-----------------------------------------------------------------------------------------------
if __name__ == "__main__":  # Hauptprogramm
    fenster = tk.Tk()
    program = Program(fenster)
    fenster.mainloop()
#-----------------------------------------------------------------------------------------------
