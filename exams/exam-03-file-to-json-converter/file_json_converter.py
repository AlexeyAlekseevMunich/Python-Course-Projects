#Teilpüfung_03
#Namen aus Text Datei laden. Datei vorhanden - namen.txt. Und liegt in gleichem Verzeichnis.
#Daten in Json Format umwandeln. In Json Datei speichern. Datei automatisch erstellen und in desselbem Ordner speichern.
#Menü mit drei Optionen.
#Skript darf nur direkt gestartret werden.

import json  #Brauchen json Modul
namen = []   #Globale Variable für die Namen. Für die Prüfung in speichere_namen():, falls nicht vorhanden.

#---------------------------------------------------------------------------------------------------------------
def lese_namen(datei="namen.txt"):    #Aus Datei Namen lesen
    global namen  #Zugriff auf globale Variable, wird gespeichert
    try:
        with open(datei, 'r', encoding='utf-8') as file:   #öffnen Datei als "reden"
            for name in file:
                namen.append(name.strip())  #in Variable Namen hinzufügen ohne Lehrzeichen
            if namen:
                print("Geladene Namen:", namen)
    except FileNotFoundError:  #Prüfung, ob Datei existier
        print("Fehler: Die Datei wurde nicht gefunden.")
    except Exception as e: #Prüfung alle andere Fehler
        print(f"Ein Fehler ist aufgetreten: {e}")

#-------------------------------------------------------------------------------------------------------------
def speichere_namen(): #Namen umwandeln und speichern
    while not namen: #Prüfen, ob Namen geladen sind
        print("Keine Namen gefunden. Bitte zuerst die Namen aus der Datei laden.")
        menue()

    json_string = json.dumps(namen, indent=4)       # Umwandlung der Namen in einen JSON-String

    json_datei = "namen.json"
    try:
        with open(json_datei, 'w', encoding='utf-8') as file:
            file.write(json_string)      # JSON-String in Datei schreiben
        print(f"Die Namen wurden erfolgreich in {json_datei} gespeichert.")
    except Exception as e:  #Fehlerprüfung
        print(f"Fehler beim Speichern der JSON-Datei: {e}")

#--------------------------------------------------------------------------------------------------------------
def menue():      #Benutzeroberfläche mit drei Varianten
    while True:
        print("\nMenü:")
        print("1 - Namen aus Datei lesen")
        print("2 - Namen als JSON speichern")
        print("3 - Beenden")
        auswahl = input("Wähle eine Option: ")
        
        if auswahl == "1":
            lese_namen()
        elif auswahl == "2":
            speichere_namen()
        elif auswahl == "3":
            print("Programm beendet.")
            break
        else:
            print("Ungültige Eingabe, bitte erneut versuchen.")

#--------------------------------------------------------------------------------------------------------------
if __name__ == "__main__":        #nur beim direkten Start von Skript. Sicherung von anderen Modulen. 
    menue()
