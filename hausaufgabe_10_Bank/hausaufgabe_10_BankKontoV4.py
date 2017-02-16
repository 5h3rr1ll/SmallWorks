#! /usr/bin/env python
# -*- coding: utf-8 -*-

from sys import exit

class Bank(object):

    def __init__(self):
        self.Bankname = "FairBank"

        self.KontoNummernLstFile = open("KontoNummernLst.txt", "r+").readline()
        for Entry in self.KontoNummernLstFile:
            self.KontoNummernLst.append(Entry.strip(" "))
        self.KontoNummernLst = []

        self.KontoNrKundenDicFile = open("KontoNrKundenDic.txt", "r+").readline()
        for Entry in self.KontoNrKundenDicFile:
            Entry = Entry.strip(" ")
            self.KontoNrKundenDic[Entry[0]] = Entry[1]
        self.KontoNrKundenDic = {}

        self.KundenLstFile = open("KundenLst.txt", "r+").readline()
        for Entry in self.KundenLstFile:
            Entry = Entry.strip(" ")
            self.KontoNrKundenDic[Entry[0]] = Entry[1]
        self.KundenLst = []

        self.KundenNameKundenNrDicFile = open("KundenNameKundenNrDic.txt", "r+").readline()
        for Entry in self.KundenNameKundenNrDicFile:
            Entry = Entry.strip(" ")
            self.KontoNrKundenDic[Entry[0]] = Entry[1]
        self.KundenNameKundenNrDic = {}


    def KontoNummernAnzeigen(self):
        print(self.KontonNummernLst)

    def KundenAnzeigen(self):
        print(self.KundenLst)

    def KundenMitKontoNummerAnzeigen(self):
        print(self.KontoNrKundenDic)

    def KontoNummerGenerator(self):
        self.NeueKontonummer = max(self.KontoNummernLst) + 1
        self.KontoNummernLst.append(self.NeueKontonummer)
        return self.NeueKontonummer


class Konto(Bank):

    def __init__(self, Kontonummer = None, KontoBesitzer = None):
        self.KontoNummern = Kontonummer
        self.KontoBesitzer = KontoBesitzer

    def KontentandAnzeigen(self):
        pass

    def Einzahulung(self):
        pass

    def Auszahlung(self):
        pass

    def Ueberweisung(self):
        pass

    def KontoInfosAnz(self):
        pass

    def Beenden():
        pass

class Kunde(Konto):#Konto):
    pass
    # self.KundenNr = ""
    # self.KontoNummer = ""

class BankMA(Konto):#Bank, Konto):
    pass
    # self.MANr = ""
    # self.MAName = ""

    def KundeAnlegen(self):
        pass

    def KontoErstellen(self):
        pass

    def KundenAufrufen(self):
        pass

    def KundenSuche(self):
        pass

    def KundenKontoAnpassen(self):
        pass

class Menue(object):
    def Exit(self):
        exit(0)

class KundenMenue(Kunde, Menue):
    def StartMenueKD(self):
        while True:
            print("1: Auszahlung")
            print("2: Einzahlung")
            print("3: Überweisung")
            print("4: Ende")


class BankMitarbeiterFrontEnd(BankMA, Menue):
    def StartMenueMA(self):
        while True:
            print("1: Kunden anlegen")
            print("2: Konto eröffnen")
            print("3: Kontoinformationen anzeigen")
            print("4: Kunden-Konto anpassen")
            print("5: Kundensuche")
            print("6: Ende")

class BankFrontEnd(BankMA, Kunde, Menue):
    def StarteMenue(self):
        while True:
            print("1: Kontonummern Anzeigen")
            print("2: Kunden Anzeigen")
            print("3: Kunden mit Kontonummer anzeigen")
            print("4: Kunden-Konto anpassen")
            print("5: Kundensuche")
            print("6: Ende")

            self.UserInput = int(input())

            if self.UserInput == 1:
                self.KontoNummernAnzeigen()
            if self.UserInput == 6:
                self.Exit()

Bank = BankFrontEnd()
Bank.StarteMenue()
