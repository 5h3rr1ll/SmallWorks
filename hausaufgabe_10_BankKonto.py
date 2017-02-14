#! /usr/bin/env python
# -*- coding: utf-8 -*-

from sys import exit

class Konto(object):
    def __init__(self, Kontostand=0, MaxUmsatz=1500, TagesUmsatz=1500):
        self.Umsatz = 0
        self.Kontostand = Kontostand
        self.MaxUmsatz = MaxUmsatz
        self.TagesUmsatz = TagesUmsatz
        self.Beispiel = 230

    def Einzahlung(self):
        self.Betrag = int(input("Wie viel möchten Sie einzahlen? "))
        if self.Umsatz <= self.TagesUmsatz:
            self.Kontostand += self.Betrag
            self.Umsatz += self.Betrag
            print("\nEs wurden {}€ eingezahlt.\n".format(self.Kontostand))
            print("Ihr neuer Kontostand lautet: {}€\n".format(self.Kontostand))
        else:
            Limit()

    def Auszahlung(self, Betrag=0):
        self.Betrag = int(input("Welchen Betrag möchten Sie abheben?: "))
        if self.Umsatz <= self.TagesUmsatz and self.Kontostand > self.Betrag:
            self.Kontostand -= self.Betrag
            self.Umsatz += self.Betrag
            print("Sie habe {}€ abgehoben. Ihr neuer Kontostand lautet {}€\n".format(self.Betrag, self.Kontostand))
        else:
            Limit()
    def ZeigeKontostand(self):
        print("\nDer Kontostand beläuft sich auf {}€.\n".format(self.Kontostand))

    def Ueberweisung(self, An="MaxMustermann", Betrag=0):
        self.An = input("Geben Sie den Namen des Empfängers an: ")
        self.Betrag = int(input("Wie viel möchten Sie überweisen: "))
        if self.Betrag < 0:
            print("Es können nur positive Beträge überwiesen werden.")
            self.Antwort = input("(N)euen Betrag eingeben oder (a)bbrechen - N / A: ")
            if self.Antwort == "N":
                return
            else:
                return Menue()
        if self.Umsatz <= self.TagesUmsatz:
            self.Kontostand -= self.Betrag
            print("\nSie haben {}€ an {} überwiesen.".format(self.Betrag, self.An))
            print("Ihr neuer Kontostand lautet {}€\n".format(self.Kontostand))
        else:
            Limit()

    def Limit(self):
        print("Die Aktion konnte leider nicht ausgeführt werden.")
        print("Ihr Tagesumsatz ist auf {}€ begrenz".format(self.Tagesumsatz))
        print("Sie können heute noch einen Transaktion im Wert von {}€ ausführen".format(self.TagesUmsatz-self.Umsatz))

    # def KontoNr(self):
    #     self.Kontonummer = 0
    #     self.KontoNrLst = []

    def KontoErstellen(self, Name="MaxMustermann", Kontonummer=1):
        self.Name = input("Geben Sie bitte Ihen Namen ein: ")
        self.Kontonummer = Kontonummer
        # self.UserKontonummer = self.Kontonummer+1
        # self.KontoNrLst.append(self.UserKontonummer)
        # self.Kontonummer += 1
        print("\nEs wurde ein Konto für {} erstellt, mit der Kontonummer {}\n".format(self.Name, self.Kontonummer))
        print("Der aktuelel Kontostand lautet: {}€\n".format(self.Kontostand))

    def Exit(self):
        print("Aufwiedersehen.")
        exit()

def Menue():
    konto = Konto()

    # Aktion = {1: "KontoErstellen()", 2: "Einzahlung()", 3: "Auszahlung()", 4: "ZeigeKontostand()", 5: "Ueberweisung()", 6:"Exit()"}

    while True:
        print("Was dürfen wir für Sie tun?: ")
        print("1: Konto erstellen")
        print("2: Einzahlen")
        print("3: Auszahlen")
        print("4: Kontostandabfragen")
        print("5: Überweisung tätigen")
        print("6: Beenden")

        userInput = int(input())

        if userInput == 1:
            konto.KontoErstellen()
        elif userInput == 2:
            konto.Einzahlung()
        elif userInput == 3:
            konto.Auszahlung()
        elif userInput == 4:
            konto.ZeigeKontostand()
        elif userInput == 5:
            konto.Ueberweisung()
        elif userInput == 6:
            konto.Exit()
        elif userInput == 7:
            print(konto.Umsatz)

Menue()

# anthony = Konto("Anthony",123456)
#
# anthony.Einzahlung(1000)
# anthony.ZeigeKontostand()
# anthony.Auszahlung(600)
# anthony.ZeigeKontostand()
# anthony.Ueberweisung("Meral",500)
