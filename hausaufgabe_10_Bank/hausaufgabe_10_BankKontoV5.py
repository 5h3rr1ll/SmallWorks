#! /usr/bin/env python
# -*- coding: utf-8 -*-

from sys import exit
# from os import path
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


        self.KDNameKtoNrDic = {}
        with open("KDNameKtoNrDic.txt","a+") as self.KDNameKtoNrDicFile:
            for Entry in self.KDNameKtoNrDicFile:
                Entry = Entry.strip()
                Entry = Entry.split(" ")
                self.KDNameKtoNrDic[Entry[0]] = Entry[1]


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
            self.KDNameKtoNrDicFile.write("{} {}".format(self.Nachname, self.Kto))

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
