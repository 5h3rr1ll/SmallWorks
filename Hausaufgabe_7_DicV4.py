#! /usr/bin/env python
# -*- coding: utf-8 -*-

def OpenFileToDic():
    """Erstellt aus einer einfach strukturieren Textdatei ein verwendbares
    Dictionary mit der Varibel dic und einer Schlüssel-Liste mit der Variabel
    dicKeys"""
    dic = {}

    # Indem der Dateiname bzw. der Dateipfad einer Variabeln zugewiesen wird, kann
    # kann, sofern vorhanden, die Datei flexibel an mehreren Stellen gleichzeitig ver-
    # ändert werden.
    File = "dic.txt"

    FileVar = open(File, "r")

    for line in FileVar:
        line = line.strip()
        Woerter = line.split(" ")
        dic[Woerter[0]] = Woerter[1]
    FileVar.close()

    # Eine Liste, die lediglich die Schlüssel aus dem Dictionary beinhaltet
    dicKeys = dic.keys()

    return dicKeys, dic

# übergebe die Returns an die Varibeln um sie in den folgenden Funktionen nutzen
# zu können.
dicKeys, dic = OpenFileToDic()


def LaenderDic():
    """In diese Fuktion können die Englische Namen von Ländern eingegebne werden
    und werden, sofern vorhanden, auf Deutsch wiedergegben. Wenn nicht vorhanden
    scheint eine dementsprechende Meldung."""

    EnglischesWort = input("Gib den englischen Namen eines Landes, speichern oder beeden ein: ")

    NeuesEngWort = ""
    DeutschesWort = ""

    # Das Programm soll erst aufhören, wenn proaktiv ein Exit verlangt wird. Ich hab
    # das Schlüsselwort "beenden" dazugenommen, das am Ende das Selbe macht wie speichern,
    # ich fand beenden einfach nur generischer.
    while True:
        if EnglischesWort in dicKeys and EnglischesWort != "speichern" and EnglischesWort != "beenden":
            print(dic[EnglischesWort])
            return LaenderDic()

        elif EnglischesWort not in dicKeys and EnglischesWort != "speichern" and EnglischesWort != "beenden":
            userInput = input("Sorry, das Land ist nicht im Wörterbuch. Möchten Sie es hinzufügen? J/N ")

            if userInput in ["J", "j", "Ja", "ja", "JA"]:

                # Der User wird zur korrekten Einfabe gezwungen! Die Eingabe muss min. 2 Zeichen
                # lang sein, vorher geht es nciht weiter
                NeuesEngWort = EnglischesWort

                while len(DeutschesWort) < 2:
                    DeutschesWort = input("\n Geben Sie nun bitte den deutschen Namen ein: ")
                    if len(DeutschesWort) < 2:
                        print("\n Das Land sollte mindest mit zwei Buchstaben geschrieben werden. ;)")
                        continue
                else:
                    dic[NeuesEngWort] = DeutschesWort
                    print("Die Einträge {} und {} wurden erfolgreich hinzugefügt.\n".format(NeuesEngWort, DeutschesWort))
                    print(dic)
                    return LaenderDic()

            elif userInput in ["N", "n", "Nein", "nein", "NEIN", "No", "NO" "no"]:
                return LaenderDic()

        elif EnglischesWort == "speichern" or EnglischesWort == "beenden":
            neueDatei = "dicV2.txt"
            fopen = open(neueDatei, "w")

            for wort in dic:
                fopen.write("{0} {1}\n".format(wort, dic[wort]))
            fopen.close()
            break

LaenderDic()
