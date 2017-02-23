from hausaufgabe_10_BankKontoV5 import Bank
from anzeige import Menue


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

Bank = BankFrontEnd()
