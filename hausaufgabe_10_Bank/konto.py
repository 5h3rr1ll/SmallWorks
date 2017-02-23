import time

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
