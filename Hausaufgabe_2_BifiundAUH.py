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
    naechsterGeburtstag = (geburtsdatumAktuellesJahr - heute).days

    kleiner30 = "Hey {0}, du hast ja in {1} Tagen Geburtstag!".format(name, naechsterGeburtstag)
    kleiner1977 = "Oha, du bist ja BiFi!"
    groesser1977 = "Na gut, noch uHu (unter Hundert)."

    if naechsterGeburtstag < 30 and int(geburtsjahr) < 1977:
        print(kleiner30 + kleiner1977)
    elif naechsterGeburtstag < 30 and 1977 < int(geburtsjahr):
        print(kleiner30 + groesser1977)
    elif int(geburtsjahr) < 1977:
        print(kleiner1977)
    elif 1977 < int(geburtsjahr):
        print(groesser1977)

Geburstag()
