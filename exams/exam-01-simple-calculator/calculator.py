# Taschenrechner Programm
# Zuerst Name und erste Frage mit Operation
print('Taschenrechner Programm!')

# Schleife für wiederholte Berechnungen
while True:
    # Auswahl der Operation
    Operation = input('Bitte wählen Sie eine Operation mit dem Buchstaben: \n A für Addition  \n S für Subtraktion \n M für Multiplikation \n D für Division \n Eingabe: ')

    # Gültige Eingaben festlegen. Und falsche aussortieren (Alle, die in der Liste sind)
    while Operation not in ['A', 'S', 'M', 'D']:
        print('Eingabe nicht korrekt, bitte noch mal eingeben. Beachte Großschreibung und Leerzeichen')
        Operation = input('Bitte wählen Sie eine Operation mit dem Buchstaben: \n A für Addition  \n S für Subtraktion \n M für Multiplikation \n D für Division \n Eingabe: ')

    # Rechnung für Addition
    ###########################################################################################################################
    if Operation == 'A':
        erlaubte_zeichen = {'0', '1', '2', '3', '4', '5', '6', '7', '8', '9', '-', '.'}  #Menge mit erlaubten Eingaben
        valid_input = False #boolische Hilfsvariable
        while not valid_input:
            Z1 = input('Addition: Geben Sie die erste Zahl: ')
            valid_input = True
            for i in Z1:   # Eingabe ist ein str mit undefinierter Anzahl. So muss jeder Element geprüft werden.
                if i not in erlaubte_zeichen:
                    valid_input = False 
                    print("Fehler: Ungültige Eingabe! Bitte nur Zahlen, '-', oder '.' eingeben.")
                    break
            if valid_input:
                Z1 = float(Z1) #Umwandlung

        valid_input = False   # genauso für Zahl 2
        while not valid_input:
            Z2 = input('Addition: Geben Sie die zweite Zahl: ') 
            valid_input = True
            for i in Z2:
                if i not in erlaubte_zeichen:
                    valid_input = False
                    print("Fehler: Ungültige Eingabe! Bitte nur Zahlen, '-', oder '.' eingeben.")
                    break
            if valid_input:
                Z2 = float(Z2) #Umwandlung

        Addition = Z1 + Z2   #Rechnung
        print(f'Ergebnis für die Addition ist: {Addition}')

    # Rechnung für Subtraktion
    ###########################################################################################################################
    elif Operation == 'S':
        erlaubte_zeichen = {'0', '1', '2', '3', '4', '5', '6', '7', '8', '9', '-', '.'}
        valid_input = False
        while not valid_input:
            Z1 = input('Subtraktion: Geben Sie die erste Zahl: ') 
            valid_input = True
            for i in Z1:
                if i not in erlaubte_zeichen:
                    valid_input = False 
                    print("Fehler: Ungültige Eingabe! Bitte nur Zahlen, '-', oder '.' eingeben.")
                    break
            if valid_input:
                Z1 = float(Z1)

        valid_input = False
        while not valid_input:
            Z2 = input('Subtraktion: Geben Sie die zweite Zahl: ') 
            valid_input = True
            for i in Z2:
                if i not in erlaubte_zeichen:
                    valid_input = False
                    print("Fehler: Ungültige Eingabe! Bitte nur Zahlen, '-', oder '.' eingeben.")
                    break
            if valid_input:
                Z2 = float(Z2)
        
        Subtraktion = Z1 - Z2
        print(f'Ergebnis für die Subtraktion ist: {Subtraktion}')

    # Rechnung für Multiplikation
    ###########################################################################################################################
    elif Operation == 'M':
        erlaubte_zeichen = {'0', '1', '2', '3', '4', '5', '6', '7', '8', '9', '-', '.'}
        valid_input = False
        while not valid_input:
            Z1 = input('Multiplikation: Geben Sie die erste Zahl: ') 
            valid_input = True
            for i in Z1:
                if i not in erlaubte_zeichen:
                    valid_input = False 
                    print("Fehler: Ungültige Eingabe! Bitte nur Zahlen, '-', oder '.' eingeben.")
                    break
            if valid_input:
                Z1 = float(Z1)

        valid_input = False
        while not valid_input:
            Z2 = input('Multiplikation: Geben Sie die zweite Zahl: ') 
            valid_input = True
            for i in Z2:
                if i not in erlaubte_zeichen:
                    valid_input = False
                    print("Fehler: Ungültige Eingabe! Bitte nur Zahlen, '-', oder '.' eingeben.")
                    break
            if valid_input:
                Z2 = float(Z2)
        
        Produkt = Z1 * Z2
        print(f'Ergebnis für die Multiplikation ist: {Produkt}')
    
    # Rechnung für Division
    ###########################################################################################################################
    elif Operation == 'D':
        erlaubte_zeichen = {'0', '1', '2', '3', '4', '5', '6', '7', '8', '9', '-', '.'}
        valid_input = False
        while not valid_input:
            Z1 = input('Division: Geben Sie die erste Zahl ein: ')
            valid_input = True
            for i in Z1:
                if i not in erlaubte_zeichen:
                    valid_input = False
                    print("Fehler: Ungültige Eingabe! Bitte nur Zahlen, '-', oder '.' eingeben.")
                    break
            if valid_input:
                Z1 = float(Z1)

        valid_input = False
        while not valid_input:
            Z2 = input('Geben Sie die zweite Zahl ein: ')
            valid_input = True
            for i in Z2:
                if i not in erlaubte_zeichen:
                    valid_input = False
                    print("Fehler: Ungültige Eingabe! Bitte nur Zahlen, '-', oder '.' eingeben.")
                    break
                if Z2 == '0':     #hier noch zusätzliche Prüfung für 0
                    print('Fehler: Division durch Null ist nicht erlaubt! Geben Sie eine andere Zahl ein.')
                    valid_input = False
                    break
            if valid_input:
                Z2 = float(Z2)

        Quotient = Z1 / Z2
        print(f'Ergebnis für die Division ist: {Quotient}')

    # Frage, ob eine weitere Berechnung durchgeführt werden soll
    weiter = input("Möchten Sie eine weitere Berechnung durchführen? (ja/nein): ")
    if weiter != 'ja':
        print("Programm wird geschlossen")
        break
