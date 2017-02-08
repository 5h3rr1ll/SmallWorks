#! /usr/bin/env python
# -*- coding: utf-8 -*-

from datetime import *
import datetime

def Geburstag():
    name = input("Wie lautet deine Vorname? ")
    nachname = input("Und dein Nachname? ")
    geburtsdatum = input("Gibt deinen Geburtstag wie folgt ein: tt.mm.yyyy: ")

    geburtstag = geburtsdatum.split(".")[0]
    geburtsmonat = geburtsdatum.split(".")[1]
    geburtsjahr = geburtsdatum.split(".")[2]

    tag0 = date(1970,1,1)
    geburtstagUm = date(int(geburtsjahr), int(geburtsmonat), int(geburtstag))
    heute = date.today()
    aktuellesJahr = datetime.datetime.now().year
    geburtsdatumAktuellesJahr = date(aktuellesJahr, int(geburtsmonat), int(geburtstag))

    differenzZu0 = geburtstagUm - tag0

    naechsterGeburtstag = 0
    naechsterGeburtstag = geburtsdatumAktuellesJahr - heute

    if heute < geburtsdatumAktuellesJahr:
        naechsterGeburtstag = geburtsdatumAktuellesJahr - heute
    else:
        naechsterGeburtstag = date(aktuellesJahr+1,int(geburtsmonat), int(geburtstag))-heute

    print("Hey {0} {1}, seit dem 01.01.1970 sind {2} Tage vergangen und du hast in {3} Tagen Geburtstag!".format(name, nachname, differenzZu0.days,naechsterGeburtstag.days))
    
Geburstag()
