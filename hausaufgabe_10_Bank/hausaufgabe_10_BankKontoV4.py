#! /usr/bin/env python
# -*- coding: utf-8 -*-

from sys import exit
from os import path
import time

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


        # self.KDNameKtoNrDic = {}
        # with open("KDNameKtoNrDic.txt") as self.KDNameKtoNrDicFile:
        #     for Entry in self.KDNameKtoNrDicFile:
        #         Entry = Entry.strip()
        #         Entry = Entry.split(" ")
        #         self.KDNameKtoNrDic[Entry[0]] = Entry[1]


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

    def KDNameKtoNrSepeichern(self, Nachname, Kto):
        self.Nachname = Nachname
        self.Kto = Kto
        with open("KDNameKtoNrDic.txt","a") as self.KDNameKtoNrDicFile:
            self.KDNameKtoNrDicFile.write("{} {}\n".format(self.Nachname, self.Kto))

    def KundenMitKontoNummerAnzeigen(self):
        print(self.KDNameKtoNrDic)

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

    def Zeitstempel(self):
        self.datumHeute = int(time.strftime("%y%m%d"))
        return self.datumHeute

    def KontentandAnzeigen(self, Kontonummer):
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

    def KontoAufrufen(self):
        pass

class BankMA(object):

    def __init__(self):
        self.bank = Bank()
        self.konto = Konto()
        # self.bank.KDNameKtoNrDic()


    def KundeAnlegen(self, Vorname = "Max", Nachname = "Mustermann"):
        Vorname = input("Vorname: ")
        Nachname = input("Nachname: ")
        self.KundeAnlegenFile = open("KundenVorNachName.txt", "a")
        self.KundeAnlegenFile.write("{} {}\n".format(Vorname, Nachname))
        self.KundeAnlegenFile.close()
        return Vorname, Nachname


    def KontoErstellen(self, Vorname = "Max", Nachname = "Mustermann",\
                        Kontonummer = 0, Kontostand = 0, MaxTagesUms = 1500):
        self.Vorname = input("Vorname: ")
        self.Nachname = input("Nachname: ")
        self.Kontonummer = self.bank.KontoNummerGenerator()
        self.Kontostand = Kontostand
        self.Erstellungsdatum = self.konto.Zeitstempel()
        print("Soll direkt Geld eingezahlt werden? J / N\n")
        Antwort = input()
        if Antwort in ["J","j","Ja","ja"]:
            print("\nWie viel wird zur Eröffnung eingezahl?")
            self.Kontostand = int(input())
        else:
            self.Kontostand = 0
        self.MaxTagesUms = MaxTagesUms
        self.LetzterUms = 0
        with open("./konten/" + self.Vorname + self.Nachname + ".txt","a") as KundenFile:
            KundenFile.write("Name [{} {}]\nKontonummer {}\nKontostand"\
            " {}\nMaxTagesUms {}\nErstellungsdatum(JJMMTT) {}\nLet.Umsatz {}".format(self.Vorname, \
            self.Nachname, self.Kontonummer, self.Kontostand, self.MaxTagesUms,\
            self.Erstellungsdatum, self.LetzterUms))

        print("\nEs wurde ein Konto für {} {}, mit der Kontonummer {} und einer \
Einzahlung von {}€ angelegt.\n".format(self.Vorname, self.Nachname, \
                self.Kontonummer, self.Kontostand))

        self.bank.KDNameKtoNrSepeichern(self.Nachname, self.Kontonummer)


    # Mit dieser Funktion soll das ein Konto, mit den Hinterlegten Informtionen
    # eines Kunden aufgerufen werden.
    def KundenAufrufen(self, Name = "", Nachname = ""):
        self.KDName = input("Vorname: ")
        self.KDNachname = input("Nachname: ")
        self.KDKontonummer = 0
        self.KDKontostand = 0
        self.KDTagesUmsMax = 0
        self.TmpDic = {}

        with open("./konten/" + self.KDName + self.KDNachname + ".txt") as KDFile:
            for line in KDFile:
                line = line.strip()
                line = line.split(" ")
                self.TmpDic[line[0]] = line[1]
            self.KDKontonummer = self.TmpDic["Kontonummer"]
            self.KDKontostand = self.TmpDic["Kontostand"]
            self.KDTagesUmsMax = self.TmpDic["MaxTagesUms"]

        print("\nName: {Vorname} {Nachname}\nKontonummer: {Kontonummer}\nKontostand:"\
        " {Kontostand}\nMaxTagesUms: {MaxTagesUms}".format(Vorname = self.KDName,\
        Nachname = self.KDNachname, Kontonummer = self.KDKontonummer, \
        Kontostand = self.KDKontostand, MaxTagesUms = self.KDTagesUmsMax))

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
            # print("4: Kunden-Konto anpassen")
            # print("5: Kundensuche")
            print("6: Ende")
            self.UserInput = int(input("Bitte treffen Sie Ihre Wahl: "))

            if self.UserInput == 1:
                self.bankMA.KontoErstellen()

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
            # print("3: Kunden mit Kontonummer anzeigen")
            # print("4: Kunden-Konto anpassen")
            # print("5: Kundensuche")
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
