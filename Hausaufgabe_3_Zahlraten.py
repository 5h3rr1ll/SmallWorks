#! /usr/bin/env python
# -*- coding: utf-8 -*-

def rateGeheimnis():
    Geheimnis = 1337
    UserZahl = 0
    Versuch = 0

    while UserZahl != Geheimnis:
        UserZahl = int(input("gib eine Zahl ein: "))
        if UserZahl == Geheimnis:
            print("Jawohl, richtig!")
            break
        elif UserZahl < Geheimnis:
            print("Zahl ist zu klein.")

        elif UserZahl > Geheimnis:
            print("Zahl zu groß.")
            

rateGeheimnis()
