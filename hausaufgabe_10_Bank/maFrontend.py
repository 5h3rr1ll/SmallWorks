from bankMA import BankMA
from anzeige import Menue

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

MA = BankMitarbeiterFrontEnd()
