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
neuerText = ""
#in dieser For-Schleife füge ich die Liste splitText wieder zu einem String zusammen,
#um ihn dann mit dem nächsten Splitt ohne Leerstellen erneut auseinander zu nehmen
for e in splitText:
    e = e.lower()
    neuerText += "{0} ".format(e)
#in diesem split werden Leerstellen ignoriert, unter anderem auch die, die im ersten
#Split entstanden sind.
splitTextV2 = neuerText.split()

neueLst = []
WortListe = []
ZaehlerListe = []

def WortZaehler():
    count = 0
    for i in splitTextV2:
        if i not in WortListe:
            WortListe.append(i)
            ZaehlerListe.append(splitTextV2.count(i))
            neueLst.append([WortListe[count], ZaehlerListe[count]])
            count += 1

    #print(neueLst)

WortZaehler()

print(splitTextV2)

def undWieOft(wort):
    SuchVersuch = 0
    for w in neueLst:
        if wort == neueLst[SuchVersuch][0]:
            print("Das wort '{0}' kam {1} in dem Text vor".format(wort, neueLst[SuchVersuch][1]))
            break
        else:
            SuchVersuch += 1
            continue

undWieOft(input("Von welchem Wort willst du die Häufigkeit wissen? "))
