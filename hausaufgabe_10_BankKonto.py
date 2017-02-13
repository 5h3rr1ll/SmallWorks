#! /usr/bin/env python
# -*- coding: utf-8 -*-

class Konto(object):
    def __init__(self, Kontostand=0, MaxUmsatz=1500, TagesUmsatz=1500):
        self.Umsatz = 0
        self.Name = Name
        self.Kontonummer = Kontonummer
        self.Kontostand = Kontostand
        self.MaxUmsatz = MaxUmsatz
        self.TagesUmsatz = TagesUmsatz
        self.Beispiel = 230

    def Einzahlung(self, Betrag):
        if self.Umsatz <= self.TagesUmsatz:
            self.Kontostand += Betrag
            self.TagesUmsatz += Betrag
        else:
            Limit()

    def Auszahlung(self, Betrag):
        if self.Umsatz <= self.TagesUmsatz:
            self.Kontostand -= Betrag
            self.TagesUmsatz += Betrag
        else:
            Limit()
    def ZeigeKontostand(self):
        print(self.Kontostand, self.Beispiel)

    def Ueberweisung(self, An, Betrag):
        if self.Umsatz <= self.TagesUmsatz:
            self.Kontostand -= Betrag
            print("Sie haben {}€ an {} überwiesen.".format(Betrag, An))
            print("Ihr neuer Kontostand lautet {}€".format(self.Kontostand))
        else:
            Limit()

    def Limit(self):
        print("Die Aktion konnte leider nicht ausgeführt werden.")
        print("Ihr Tagesumsatz ist auf {}€ begrenz".format(self.Tagesumsatz))
        print("Sie können heute noch einen Transaktion im Wert von {}€ ausführen".format(self.TagesUmsatz-self.Umsatz))

    def KontoErstellen(self, Name=ḾaxMusermann, Kontonummer=123456):
        self.Name = input("Geben Sie bitte Ihen Namen ein: ")
        self.Kontonummer = int(input("Suchen Sie Sich eine Kontonummer aus und geben Sie ein: "))


Aktion = {1: KontoErstellen(); 2: Einzahlung(), 3: Auszahlung(), 4: ZeigeKontostand(), 5: Ueberweisung(), 6:  }

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
        aktion[userInput]
    elif userInput == 2:
        Aktion[2]
    elif userInput == 3:
        Aktion[]
anthony = Konto("Anthony",123456)

anthony.Einzahlung(1000)
anthony.ZeigeKontostand()
anthony.Auszahlung(600)
anthony.ZeigeKontostand()
anthony.Ueberweisung("Meral",500)
