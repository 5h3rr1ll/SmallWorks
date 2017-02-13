#! /usr/bin/env python
# -*- coding: utf-8 -*-

class Konto(object):
    def __init__(self, Name, Kontonummer, Kontostand=0, MaxUmsatz=1500, TagesUmsatz=0):
        self.Name = Name
        self.Kontonummer = Kontonummer
        self.Kontostand = Kontostand
        self.MaxUmsatz = MaxUmsatz
        self.TagesUmsatz = TagesUmsatz

        print(Name, Kontostand, MaxUmsatz, TagesUmsatz)

        return Name,Kontostand,Kontonummer,MaxUmsatz,TagesUmsatz

    def Einzahlung(self, Betrag):
        Kontostand += Betrag
        TagesUmsatz += Betrag

    def Auszahlung(self, Betrag):
        Kontostand -= Betrag
        TagesUmsatz += Betrag

    def ZeigeKontostand(self):
        print(Kontostand)


anthony = Konto("Anthony",123456)

anthony.Einzahlung(1000)
anthony.ZeigeKontostand
anthony.Auszahlung(100)
anthony.ZeigeKontostand
