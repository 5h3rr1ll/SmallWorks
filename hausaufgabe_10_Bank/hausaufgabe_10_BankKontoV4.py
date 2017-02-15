#! /usr/bin/env python
# -*- coding: utf-8 -*-

from sys import exit

class Bank(object):
    self.Bankname
    self.Kontos
    self.KontoNummern
    self.Kunden

    def KontosAnzeigen(self):
        pass

    def KontoNummernAnzeigen(self):
        pass

    def KundenAnzeigen(self):
        pass


class Konto(Bank):

    self.KontoNummern
    self.KontoBesitzer

    def KontostandAnzeigen(self):
        pass

    def Einzahulung(self):
        pass

    def Auszahlung(self):
        pass

    def Ueberweisung(self):
        pass

    def KontoInfosAnz(self):
        pass

class Kunde(Konto):
    self.KundenNr
    self.KontoNummern

class BankMA(Bank, Konto):
    self.MANr
    self.MAName

    def KundeAnlegen(self):
        pass

class KundenMenue(Kunde):

class MAMaske(BankMA, Bank, Konto)
