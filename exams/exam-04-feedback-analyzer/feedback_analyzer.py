#Teilprüfung_04
#Analyse von Textdatei mit Kundenfeedback aus verschiedenen Ländern
#Textdatei vorhanden (selber erstellt: "feedback.txt" und liegt in gleichem Verzeichnis)
#Zuerst einzelne Funktionen, dann einzeln durchführen und zur Prüfung darstellen. 
#Alle möglichen Fehler abfangen

#Brauchen Module: json und re
import re
import json

#--------------------------------------------------------------------------------------------------------------------------------------------------------------
def lese_feedback(dateiname="feedback.txt"):    #Datei feedback.txt lesen und gibt den gesamten Inhalt als Liste von Zeilen zurück.
    try:
        feedback_list = []     #Liste anlegen
        with open(dateiname, "r", encoding="utf-8") as file:     #öffnen mit UTF-8 Encoding
            next(file)     # Überspringe die erste Zeile
            for line in file:
                feedback_list.append(line.strip())      #Entfernt Leerzeichen/Zeilenumbrüche
        return feedback_list       #Liste mit Zeilen
    except FileNotFoundError:  
        print("Fehler: Die Datei wurde nicht gefunden! \U0001F6D1")  # Warnung Emoji
        return None  #None beim Fehler
    except Exception as e:
        print(f"Ein unerwarteter Fehler ist aufgetreten: \U000026D4 {e}")  # Rotes Kreuz Emoji
        return None  

#------------------------------------------------------------------------------------------------------------------------------------------------------------------
def extrahiere_datumsangaben(feedback_list):     # Extrahiert alle Datumsangaben im Format DD.MM.YYYY aus einer Liste von Feedback-Zeilen.
    try:
        if not feedback_list:
            print("Kein Feedback gefunden.")
            return []  # Leere Liste, falls keine Daten
        datum_pattern = r"\b\d{2}\.\d{2}\.\d{4}\b"   # Regulärer Ausdruck für das Datumsformat DD.MM.YYYY
        datums_liste = []    # Liste für Datumsangaben
        for line in feedback_list:
            datums_liste += re.findall(datum_pattern, line)  # Alle Datumsangaben in der aktuellen Zeile hinzufügen
        if datums_liste:
            print("Datumsangaben erfolgreich extrahiert! \U00002705")  # Häkchen Emoji
            return datums_liste  #Gefundenen Datumsangaben
        else:
            print("Es wurden keine Datumsangaben im Format DD.MM.YYYY gefunden. \U00002139")  # Info Emoji
            return []
    except Exception as e:
        print(f"Fehler bei der Extraktion der Datumsangaben: \U000026D4 {e}")  # Fehler Emoji
        return []  # Leere Liste bei Fehler

#---------------------------------------------------------------------------------------------------------------------------------------------
def zaehle_datumsangaben(datums_liste):    #Daten zählen
    """Zählt, wie oft jedes Datum vorkommt, und gibt ein Dictionary mit Datum als Schlüssel und Vorkommen als Wert zurück."""
    try:
        if not datums_liste:
            print("Keine Datumsangaben zum Zählen vorhanden.")  # Text, keine Emojis
            return {}
        datum_zaehlung = {} #Dict initialisieren 
        for datum in datums_liste:
            if datum in datum_zaehlung:
                datum_zaehlung[datum] += 1  #Datum
            else:
                datum_zaehlung[datum] = 1  #neue Datum
        return datum_zaehlung
    except Exception as e:
        print(f"Fehler beim Zählen der Datumsangaben: \U000026D4 {e}")  # Rotes Kreuz Emoji
        return {} 

#------------------------------------------------------------------------------------------------------------------------------------------------
def finde_exzellente_kommentare(feedback_list):  #nach "exzellent" suchen
    try:
        exzellente_kommentare = []
        for kommentar in feedback_list:
            if re.findall(r"\bexzellent\b", kommentar.lower()):  #Kommentar in Kleinbuchstaben umwandeln
                exzellente_kommentare.append(kommentar)  #Kommentar zur Liste hinzufügen
        return exzellente_kommentare  #Liste
    except Exception as e:
        print(f"Fehler beim Finden der exzellenten Kommentare: \U000026D4 {e}")  # Rotes Kreuz Emoji
        return [] 
    
#----------------------------------------------------------------------------------------------------------------------------------------------------
def speichere_daten_in_json(dateiname, daten):  #Speichert die Daten in einer JSON-Datei.
    try:
        with open(dateiname, 'w', encoding="utf-8") as json_file: #
            json.dump(daten, json_file, indent=4)
        print(f"Daten wurden erfolgreich in {dateiname} gespeichert. \U00002705")  # Häkchen Emoji
    except Exception as e:
        print(f"Fehler beim Speichern der Daten in {dateiname}: \U000026D4 {e}")  # Rotes Kreuz Emoji

#-----------------------------------------------------------------------------------------------------------------------------------------------------
#Aufruf der Funktionen. Auch zur Prüfung und Darstellung.
#Zuerst die Datei lesen
feedback_list = lese_feedback()  
if feedback_list:
    print("Feedback-Inhalt:")
    for line in feedback_list:
        print(line)

    #Datum extrahieren
    datumsangaben = extrahiere_datumsangaben(feedback_list)
    print("\nExtrahierte Datumsangaben:")
    for datum in datumsangaben:
        print(datum)

    #Zählen, wie oft jedes Datum vorkommt
    datum_zaehlung = zaehle_datumsangaben(datumsangaben)
    print("\nGefundene Datumsangaben und ihre Häufigkeit:")
    for datum, anzahl in datum_zaehlung.items():
        print(f"{datum}: {anzahl} mal")

    #Finden exzellente Kommentare
    exzellente_kommentare = finde_exzellente_kommentare(feedback_list)
    print("\nKommentare, die das Wort 'exzellent' enthalten:")
    for kommentar in exzellente_kommentare:
        print(kommentar)

    # Leere Zeile einfügen (Einfach Trennung in Anzeige)
    print()

    # Speichern der Daten in JSON-Dateien
    speichere_daten_in_json("datums_vorkommen.json", datum_zaehlung)  # Speichern der Datumsvorkommen
    speichere_daten_in_json("exzellente_feedbacks.json", exzellente_kommentare)  # Speichern der exzellenten Kommentare
