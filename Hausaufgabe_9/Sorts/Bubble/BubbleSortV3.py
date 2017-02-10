#! /usr/bin/env python
# -*- coding: utf-8 -*-

def BubbleSort():
    """ Sortiert die Zahlen von klein nach groß. Erwartet eine Listen-Objekt, gefüllt
    mit Zahlen. """

    ZahlenLst = []
    ZahlenLst += input("Gib die Zahlen mit komma getrennt, keine Leerzeichen, ein, die sortiert werden sollen: ")

    print(ZahlenLst) #damit man sieht welche Liste mit Zahlen eingegeben wurde
    Index = 0
    geprüft = False

    while True: # eine while-Schleif, damit sie solange weiterläuft, bist die zwei
# gewünschten Bedingungen erfüllt sind.

# der if-Part prüft lediglich ob alle Elemente der Liste geprüft wurden, wenn dem
# so ist, beendet sie die Schleife. Das ist sozusagen der Exit aus der Schleife
        if Index+1 == len(ZahlenLst) and geprüft:
            print("Fertig!")
            break

# dieses elif prüft ob die zuerst geprüfte Zahl kleiner ist als die Zweite, sollte
# dem nicht so sein, erhöt es den Index, damit das die nächsten beiden Zahlen ge-
# prüft werden können. Die Variabel geprüft wird auf True gesetzt, da wenn alle
# Elemente der Liste geprüft wurden, ohne das ein Wechsel passierte, jener die
# Variabel auf False setzt, die Schleife verlassen werden soll/kann.
        elif ZahlenLst[Index] < ZahlenLst[Index+1]:
            Index += 1
            geprüft = True

# dieses elif prüft die zwei Zahlen, sollte die Erste größer der Zweiten sein,
# wird die Zweite mit pop-Funktion aus der Liste rausgelöscht und übergeben an die
# insert-Methode, die den übergebenen Wert mit dem Index der 1. Zahl, bedingt durch
# die Methodik der Methode, vor ihr wieder eingefügt wird. Setzt dann die Variabel
# geprüft auf False, da solange die Variabel False ist, die Schleife weiterläuft.
        elif ZahlenLst[Index] > ZahlenLst[Index+1]:
            ZahlenLst.insert(Index, ZahlenLst.pop(Index+1))
            geprüft = False
            Index = 0
            print(ZahlenLst) # damit man die Zwischenergebnisse sehen kann
