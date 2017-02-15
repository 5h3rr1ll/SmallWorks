#! /usr/bin/env python
# -*- coding: utf-8 -*-

from sys import exit


class Konto(object):
    def __init__(self):
        self.Kontostand = 0
        self.MaxTagesUms = 1500
        self.TagesUmsatz = 0
        self.KundenDic = {}
        self.File = "Kunde.txt"
        self.KundenDB = open(self.File, "r")
        self.Kontonummer = 0

        for line in self.KundenDB:
            line = line.strip()
            Eintrag = line.split(" ")
            self.KundenDic[Eintrag[0]] = Eintrag[1]
        self.KundenDB.close()


    def OpenKtoNrDic(self):
        self.KtoFile = "KtoLst.txt"
        self.KtoNrFileObject = open(KtoFile)
        self.KtoNrDic = {}

        for line in self.KtoNrFileObject:
            line = line.strip()
            Eintrag = line.split(" ")
            self.KtoNrDic[Eintrag[0]] = Eintrag[1]

    def CheckKtoNr(self, Name, Kotonummer = None):
        self.OpenKtoNrDic()
        self.Name = Name
        # self.KtoNrDicKeys = self.KtoNrDic.keys()

        if self.Name not in self.KtoNrDic:
            self.UserKontonummer = (self.Kontonummer + 1)
            self.KontoErstellen(Namen, Kontonummer)
             and self.Kontonummer != self.KtoNrDic[self.Name]:
            self.KtoNrDic[self.Name] = self.Kontonummer+1
        else:



    def KontoErstellen(self, Name="MaxMustermann", Kotonummer):
        self.Name = input("Geben Sie bitte Ihen Namen ein: ")
        self.Kontonummer = Kotonummer
        print("\nEs wurde ein Konto für {} erstellt, mit der Kontonummer {}\n".format(self.Name, self.Kontonummer))
        print("Der aktuelel Kontostand lautet: {}€\n".format(self.Kontostand))
        self.KundenDic["Name"] = self.Name
        self.KundenDic["Kontonummer"] = self.Kontonummer


    def Einzahlung(self):
        print("Wie viel möchten Sie einzahlen? ")
        self.Betrag = int(input("> "))
        if (self.Betrag + self.TagesUmsatz) <= self.MaxTagesUms:
            self.Kontostand += self.Betrag
            self.TagesUmsatz += self.Betrag
            print("\nEs wurden {}€ eingezahlt.\n".format(self.Kontostand))
            print("Ihr neuer Kontostand lautet: {}€\n".format(self.Kontostand))
            self.KundenDic["Kontostand"] = self.Kontostand
        else:
            self.Limit()


    def Auszahlung(self, Betrag=0):
        print("Welchen Betrag möchten Sie abheben?")
        self.Betrag = int(input("> "))
        if (self.TagesUmsatz + self.Betrag) <= self.MaxTagesUms and self.Kontostand > self.Betrag:
            self.Kontostand -= self.Betrag
            self.TagesUmsatz += self.Betrag
            print("Sie habe {}€ abgehoben. Ihr neuer Kontostand lautet {}€\n".format(self.Betrag, self.Kontostand))
            self.KundenDic["Kontostand"] = self.Kontostand
        else:
            self.Limit()


    def ZeigeKontostand(self):
        print("\nDer Kontostand beläuft sich auf {}€.\n".format(self.Kontostand))


    def Ueberweisung(self, An="MaxMustermann", Betrag=0):
        self.An = input("Geben Sie den Namen des Empfängers an: ")
        self.Betrag = int(input("Wie viel möchten Sie überweisen: "))
        if self.Betrag > 0 and (self.Betrag + self.TagesUmsatz) < self.MaxTagesUms:
            self.Kontostand -= self.Betrag
            self.TagesUmsatz += self.Betrag
            print("\nSie haben {}€ an {} überwiesen.".format(self.Betrag, self.An))
            print("Ihr neuer Kontostand lautet {}€\n".format(self.Kontostand))
        elif (self.Betrag + self.TagesUmsatz) > self.MaxTagesUms:
            self.Limit()
        elif self.Betrag < 0:
            print("Es können nur positive Beträge überwiesen werden.")
            self.Antwort = input("(N)euen Betrag eingeben oder (a)bbrechen - N / A: ")
            if self.Antwort == "N" or self.Antwort == "n":
                self.Ueberweisung()
            elif self.Antwort == "A" or self.Antwort == "a":
                Menue()


    def Limit(self):
        print("\nDie Aktion konnte leider nicht ausgeführt werden.")
        print("Ihr Tagesumsatz ist auf {}€ begrenz".format(self.MaxTagesUms))
        print("Sie können heute noch einen Transaktion im Wert von {}€ ausführen.\n".format(self.MaxTagesUms - self.TagesUmsatz))


    def Test(self):
        print(self.KundenDic)

    def Exit(self):
        self.KundenDB = open(self.File, "w")

        for Eintrag in self.KundenDic:
            self.KundenDB.write("{0} {1}\n".format(Eintrag, self.KundenDic[Eintrag]))
        self.KundenDB.close()
        print("Aufwiedersehen.")
        exit()

def Menue():
    konto = Konto()

    # Aktion = {1: "KontoErstellen()", 2: "Einzahlung()", 3: "Auszahlung()", 4: "ZeigeKontostand()", 5: "Ueberweisung()", 6:"Exit()"}

    while True:
        print("\nWas dürfen wir für Sie tun?: \n")
        print("1: Konto erstellen")
        print("2: Einzahlen")
        print("3: Auszahlen")
        print("4: Kontostandabfragen")
        print("5: Überweisung tätigen")
        print("6: Beenden\n")

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
            pass
        elif userInput == 8:
            konto.Test()

Menue()

# anthony = Konto("Anthony",123456)
#
# anthony.Einzahlung(1000)
# anthony.ZeigeKontostand()
# anthony.Auszahlung(600)
# anthony.ZeigeKontostand()
# anthony.Ueberweisung("Meral",500)
