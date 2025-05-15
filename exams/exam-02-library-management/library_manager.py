'''
Verwaltung von Büchereien. Mit folgenden Funktionen:
Buchsuche, Buch hinzufügen, Bücher nach Jahr filtern, Anzeige der Bücherei-Datenbank.
Mit interaktivem Menü
Mit Datenbankstruktur (Beispiel):
buecherei_datenbank = [
    {"Titel": "Python lernen", "Autor": "Max Mustermann", "Jahr": 2020},
    {"Titel": "Fortgeschrittene Python-Programmierung", "Autor": "Erika Musterfrau", "Jahr": 2021},
    {"Titel": "Python lernen", "Autor": "John Doe", "Jahr": 2019}
] 
'''

#Datenbank mit Beispielen befüllen, um am Start nicht leer ist:
buecherei_datenbank = [
    {"Titel": "Python lernen", "Autor": "Max Mustermann", "Jahr": 2020},
    {"Titel": "Fortgeschrittene Python-Programmierung", "Autor": "Erika Musterfrau", "Jahr": 2021},
    {"Titel": "Python lernen", "Autor": "John Doe", "Jahr": 2019}
]

#Einzelne Funktionen definieren:---------------------------------------------------------------------
def buecherei_anzeigen():
    if buecherei_datenbank:
        print("\nBücherei-Datenbank:")
        for buch in buecherei_datenbank: #einfach alle dict in Liste ausgeben
            print(f"Titel: {buch['Titel']}, Autor: {buch['Autor']}, Jahr: {buch['Jahr']}")
    else:
        print("Die Bücherei ist leer.")
#----------------------------------------------------------------------------------------------------
def buch_suchen():
    suchbegriff = input("Bitte Titel oder Autor eingeben: ")
    
    gefundene_buecher=[] #definieren als Liste
    for buch in buecherei_datenbank:
        if suchbegriff in buch["Titel"] or suchbegriff in buch["Autor"]:
            gefundene_buecher.append(buch) #hinzufügen
    
    if gefundene_buecher:
        print("\nGefundene Bücher:")
        for buch in gefundene_buecher:
            print(f"Titel: {buch['Titel']}, Autor: {buch['Autor']}, Jahr: {buch['Jahr']}")
    else:
        print("Kein Buch gefunden.")
#---------------------------------------------------------------------------------------------------          
def buecher_nach_jahr_filtern():  #mit filter() Funktion
    jahr = input("Bitte ein Jahr eingeben: ")
    
    # Validierung, dass das Jahr eine Zahl ist
    while not jahr.isdigit(): #prüfung ob nur Zahlen
        print("Bitte hier nur Zahlen eingeben!")
        jahr = input("Bitte ein Jahr eingeben: ")
    
    jahr = int(jahr)  # Umwandeln von str zu int
    
    # Filtere Bücher nach Jahr mit Lambda Funktion. Suchen und filtern nach eingegebenen Jahr im Datenbank und erstellen die Liste
    gefundene_buecher = list(filter(lambda buch: buch["Jahr"] == jahr, buecherei_datenbank))
    
    # Ausgabe der gefundenen Bücher
    if gefundene_buecher:
        print(f"\nBücher aus dem Jahr {jahr}:")
        for buch in gefundene_buecher:
            print(f"Titel: {buch['Titel']}, Autor: {buch['Autor']}, Jahr: {buch['Jahr']}")
    else:
        print(f"Keine Bücher aus dem Jahr {jahr} gefunden.")
    
#--------------------------------------------------------------------------------------------------       
def buch_hinzufuegen(): #einzelne Abfrage
    titel = input("Bitte Titel eingeben: ")
    autor = input("Bitte Autor eingeben: ")
    jahr = input("Bitte Jahr der Veröffentlichung eingeben: ")
    
    # prüfen on nur Zahlen
    while not jahr.isdigit():
        print("Bitte hier nur Zahlen eingeben: ")
        jahr = input("Bitte Jahr der Veröffentlichung eingeben: ")
    
    jahr = int(jahr)  # Umwandeln von str zu int
    
    #Buch hinzufügen
    neues_buch = {"Titel": titel, "Autor": autor, "Jahr": jahr}
    buecherei_datenbank.append(neues_buch)
    print(f"\nBuch '{titel}' von {autor} wurde hinzugefügt.")
#-------------------------------------------------------------------------------------------------   

#interaktives Memü:        
while True:
    print("\nBücherei-Verwaltung")
    print("1. Buch suchen")
    print("2. Buch hinzufügen")
    print("3. Bücher nach Jahr filtern")
    print("4. Bücherei-Datenbank anzeigen")
    print("5. Beenden")
    
    auswahl = input("Wähle eine Option (1-5): ")
    
    if auswahl == "1":
        buch_suchen()         
    elif auswahl == "2":
        buch_hinzufuegen()        
    elif auswahl == "3":
        buecher_nach_jahr_filtern()         
    elif auswahl == "4":
        buecherei_anzeigen()           
    elif auswahl == "5":
        print("Programm beendet.")
        break  
    else:
        print("Ungültige Eingabe, bitte erneut versuchen.")

