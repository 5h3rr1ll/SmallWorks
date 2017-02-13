#! /usr/bin/env python
# -*- coding: utf-8 -*-

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
            self.TagesUmsatz += self.Betrag
        else:
            Limit()

    def Auszahlung(self, Betrag=0):
        self.Betrag = int(input("Welchen Betrag möchten Sie abheben?: "))
        if self.Umsatz <= self.TagesUmsatz and self.Kontostand > self.Betrag:
            self.Kontostand -= self.Betrag
            self.TagesUmsatz += self.Betrag
        else:
            self.Limit()
    def ZeigeKontostand(self):
        print(self.Kontostand)

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
            print("Sie haben {}€ an {} überwiesen.".format(self.Betrag, self.An))
            print("Ihr neuer Kontostand lautet {}€".format(self.Kontostand))
        else:
            Limit()

    def Limit(self):
        print("Die Aktion konnte leider nicht ausgeführt werden.")
        print("Ihr Tagesumsatz ist auf {}€ begrenz".format(self.Tagesumsatz))
        print("Sie können heute noch einen Transaktion im Wert von {}€ ausführen".format(self.TagesUmsatz-self.Umsatz))

    # def KontoNr(self):
    #     self.Kontonummer = 0
    #     self.KontoNrLst = []

    def KontoErstellen(self, Name="MaxMustermann", Kontonummer=0):
        self.Name = input("Geben Sie bitte Ihen Namen ein: ")
        self.Kontonummer = Kontonummer
        # self.UserKontonummer = self.Kontonummer+1
        # self.KontoNrLst.append(self.UserKontonummer)
        # self.Kontonummer += 1
        print("Es wurde ein Konto für {} erstellt, mit der Kontonummer {}".format(self.Name, self.Kontonummer)) #self.UserKontonummer))

    def Exit(self):
        return False

def Menue():
    konto = Konto()

    # Aktion = {1: "KontoErstellen()", 2: "Einzahlung()", 3: "Auszahlung()", 4: "ZeigeKontostand()", 5: "Ueberweisung()", 6:"Exit()"}

    while True:
        print("Was möchten Sie gerne Tun?:")
        print("1: Konto erstellen")
        print("2: Einzahlen")
        print("3: Auszahlen")
        print("4: Kontostandabfragen")
        print("5: Eine Überweisung tätigen")
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

Menue()

# anthony = Konto("Anthony",123456)
#
# anthony.Einzahlung(1000)
# anthony.ZeigeKontostand()
# anthony.Auszahlung(600)
# anthony.ZeigeKontostand()
# anthony.Ueberweisung("Meral",500)
