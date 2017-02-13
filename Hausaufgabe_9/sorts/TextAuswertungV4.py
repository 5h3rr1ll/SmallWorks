#! /usr/bin/env python
# -*- coding: utf-8 -*-

from re import split
# mit dem importiren von re (RegularExpressions) kann ich eine split-Methode nutzen
# die leditlich buchstaben und Zahlen berücksichtig, keine Sonderzeichen

#textdatei im Lesemodus öffnen. Gibt jedoch nur ein Datei-Objekt zurück
text = open("text.txt", "r")

#nun noch mit read den Text aus der Datei als String zurückgeben
text = text.read()
#hier kommt nun split von re zum einsatz. Das große \W macht das er nur buchstaben
#und Zahlen widergibt, sonderzeichen, werden als leer Elemente abgelegt
splitText = (split("\W", text))
#die Variabel benöte ich für das zweite Splitten
# neuerText = ""
#in dieser For-Schleife füge ich die Liste splitText wieder zu einem String zusammen,
#um ihn dann mit dem nächsten Splitt ohne Leerstellen erneut auseinander zu nehmen
# for e in splitText:
#     e = e.lower()
#     neuerText += "{0} ".format(e)
#in diesem split werden Leerstellen ignoriert, unter anderem auch die, die im ersten
#Split entstanden sind.
splitTextV2 = splitText.split()

dic = {}

def WortZaehler():
    """Diese Funktion gibt eine Liste zurück mit jedem Wort, das in dem Text vor
    vorkam. Mit eingabe eines der aufgelisteten Worde, bekommt man die Häufigkeit
    des Wortes in dem Text zurückgegeben."""

# Für jedes Element in der Liste splitTextV2
    for i in splitTextV2:
# Wenn das Element nicht bereits in der Liste ist:
        if i not in dic.keys():
            # Füge das Element hinzu, mit dem Wert, der die Häufigkeit des Wortes
            # in dem Ursprünglichen Text entspricht.
            dic[i] = splitTextV2.count(i)


    #print(dic)

WortZaehler()

for i in splitTextV2:
    print(splitTextV2)

def undWieOft(wort):
    print("Das wort '{0}' kam {1} in dem Text vor".format(wort, dic[wort]))

undWieOft(input("Von welchem Wort willst du die Häufigkeit wissen? "))
