from datetime import *


"""programm soll nach meinem namen und nachnamen fragen, sowie nach meinem
geburtsdatum. danch soll das prog ausgeben, wie alt ich relativ zu dem Datum
1.1.1970 bin und wie viele tage es noch dauert bis ich wieder geburtstag habe"""

def timeubung():
    vorname = input("Wie lautet dein Vorname? ")
    nachname = input("Und dein Nachname? ")
    bday = input("Wann hast du Geburstag? Bitte in folgender Form angeben tt.mm.yyyy: ")
    heute = date.today()
    print(heute)

timeubung()
