#! /usr/bin/env python
# -*- coding: utf-8 -*-

from sys import exit
from os import path

class Bank(object):

    def __init__(self):
        self.Bankname = "FairBank"

        """Eine Liste mit allen Kontonummern, damit lediglich überprüft werden
        kann, welche Kontonummern es bereits gibt. Außerdem wird aus dieser Liste
        die größte vorhandene Kontonummer ermittelt, durch das erhöhen um 1 wird
        eine neue Kontonummer generiert."""
        self.KontoNummernLst = []
        self.KontoNummernLstFile = open("KontoNummernLst.txt")
        for Entry in self.KontoNummernLstFile:
            self.KontoNummernLst.append(int(Entry.strip()))
        self.KontoNummernLstFile.close()


        self.KontoNrKundenDic = {}
        with open("KontoNrKundenDic.txt") as self.KontoNrKundenDicFile:
            for Entry in self.KontoNrKundenDicFile:
                Entry = Entry.strip()
                Entry = Entry.split(" ")
                self.KontoNrKundenDic[Entry[0]] = Entry[1]


        self.KundenLst = []
        self.KundenLstFile = open("KundenLst.txt", "r+")
        for Entry in self.KundenLstFile:
            Entry = Entry.strip()
            Entry = Entry.split(" ")
            self.KundenLst.append("{} {}".format(Entry[0], Entry[1]))
        self.KundenLstFile.close()


        self.KundenNameKundenNrDic = {}
        self.KundenNameKundenNrDicFile = open("KundenNameKundenNrDic.txt", "r+")
        for Entry in self.KundenNameKundenNrDicFile:
            Entry = Entry.strip()
            Entry = Entry.split(" ")
            self.KundenNameKundenNrDic[Entry[0]] = Entry[1]


    def KontoNummernAnzeigen(self):
        print(self.KontoNummernLst)

    def KundenAnzeigen(self):
        print(self.KundenLst)

    def KundenMitKontoNummerAnzeigen(self):
        print(self.KontoNrKundenDic)

    def KundenKontoAnpassen(self):
        pass

    def KontoNummerGenerator(self):
        self.max = max(self.KontoNummernLst)
        self.NeueKontonummer = int(self.max + 1)
        self.KontoNummernLst.append(self.NeueKontonummer)
        self.KontoNummernLstFile = open("KontoNummernLst.txt","a")
        self.KontoNummernLstFile.write(str(self.NeueKontonummer))
        self.KontoNummernLstFile.write("\n")
        self.KontoNummernLstFile.close()
        return self.NeueKontonummer


class Konto(object):

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

class Kunde(object):
    pass
    # self.KundenNr = ""
    # self.KontoNummer = ""

class BankMA(object):

    def __init__(self):
        self.bank = Bank()
        self.bank.KontoNrKundenDic()


    def KundeAnlegen(self, Vorname = "Max", Nachname = "Mustermann"):
        Vorname = input("Vorname: ")
        Nachname = input("Nachname: ")
        self.KundeAnlegenFile = open("KundenVorNachName.txt", "a")
        self.KundeAnlegenFile.write("{} {}\n".format(Vorname, Nachname))
        self.KundeAnlegenFile.close()
        return Vorname, Nachname


    def KontoErstellen(self, Vorname = "Max", Nachname = "Mustermann", Kontonummer = 0, StartBetrag = 0, MaxTagesUms = 1500):
        Vorname = input("Vorname: ")
        Nachname = input("Nachname: ")
        Kontonummer = self.bank.KontoNummerGenerator()
        print("Soll direkt Geld eingezahlt werden? J / N\n")
        Antwort = input()
        if Antwort in ["J","j","Ja","ja"]:
            print("\nWie viel wird zur Eröffnung eingezahl?")
            StartBetrag = int(input())
        else:
            StartBetrag = 0
        self.UserMaxTagesUms = MaxTagesUms
        self.KundenFile = open("./konten/" + Vorname + Nachname + ".txt","a")
        self.KundenFile.write("Name [{} {}]\nKontonummer {}\nStartBetrag {}\nMaxTagesUms {}".format(Vorname, Nachname, Kontonummer, StartBetrag, self.UserMaxTagesUms))
        self.KundenFile.close()
        print("\nEs wurde ein Konto für {} {}, mit der Kontonummer {} und einer Einzahlung von {}€ angelegt.\n".format(Vorname, Nachname, Kontonummer, StartBetrag))
        self.bank.KontoNrKundenDic[Kontonummer] = [Vorname, Nachname]

    # Mit dieser Funktion soll das ein Konto, mit den Hinterlegten Informtionen
    # eines Kunden aufgerufen werden.
    def KundenAufrufen(self, Name, Nachname):
        with open(Name + Nachname + ".txt") as KDFile:
            for line in KDFile:
                print(line)
        # self.Name = input("Vorname des Kunden: ")
        # self.Nachname = input("Nachname des Kunden: ")
        # if Kunde in KundenDic:
        #     self.KundenFile = open("./konten/" + self.Name + self.Nachname + ".txt", "r+")
        # else:
        #     print("Kunde nicht im System gefunden.")
        #     return


    def KundenSuche(self):
        self.KundenName = input("Geben Sie bitte den Name des zu suchenden Kunden ein: ")
        print(Kunden)
        pass

    def KundenKontoAnpassen(self):
        pass

class Menue(object):
    def Exit(self):
        exit(0)

class KundenMenue(Menue):
    def StartMenueKD(self):
        while True:
            print("1: Auszahlung")
            print("2: Einzahlung")
            print("3: Überweisung")
            print("4: Ende")


class BankMitarbeiterFrontEnd(Menue):
    def __init__(self):
        self.bankMA = BankMA()
        self.StartMenueMA()

    def StartMenueMA(self):
        while True:
            print("1: Konto eröffnen")
            print("2: Kundenkonto laden")
            print("4: Kunden-Konto anpassen")
            print("5: Kundensuche")
            print("6: Ende")
            self.UserInput = int(input("Bitte treffen Sie Ihre Wahl: "))

            if self.UserInput == 1:
                self.bankMA.KundeAnlegen()

            if self.UserInput == 2:
                self.bankMA.KundenAufrufen()

            if self.UserInput == 6:
                self.Exit()


class BankFrontEnd(Menue):

    def __init__(self):
        self.bank = Bank()
        self.StarteMenue()

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
                self.bank.KontoNummernAnzeigen()
            if self.UserInput == 2:
                self.bank.KundenMitKontoNummerAnzeigen()
            if self.UserInput == 3:
                self.bank.KundenMitKontoNummerAnzeigen()
            if self.UserInput == 4:
                self.bank.KundenKontoAnpassen()
            if self.UserInput == 5:
                self.bank.KundenKontoAnpassen()
            if self.UserInput == 6:
                self.Exit()

# Bank = BankFrontEnd()
MA = BankMitarbeiterFrontEnd()
