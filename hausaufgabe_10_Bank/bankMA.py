from hausaufgabe_10_BankKontoV5 import Bank
from konto import Konto

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
        " {Kontostand}\nMaxTagesUms: {MaxTagesUms}\n".format(Vorname = self.KDName,\
        Nachname = self.KDNachname, Kontonummer = self.KDKontonummer, \
        Kontostand = self.KDKontostand, MaxTagesUms = self.KDTagesUmsMax))

    def KundenSuche(self):
        self.KundenName = input("Geben Sie bitte den Name des zu suchenden Kunden ein: ")
        print(Kunden)
        pass

    def KundenKontoAnpassen(self):
        pass
