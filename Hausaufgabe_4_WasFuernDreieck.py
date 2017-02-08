#! /usr/bin/env python
# -*- coding: utf-8 -*-

def WattNDreiEck(seitenlaenge1, seitenlaenge2, seitenlaenge3):
    if (seitenlaenge1**2 + seitenlaenge2**2 == seitenlaenge3**2) or +\
    (seitenlaenge1**2 == seitenlaenge2**2 + seitenlaenge3**2) or +\
    (seitenlaenge3**2 + seitenlaenge1**2 == seitenlaenge2**2):
        print("Rechtwinklige Dreiecke")
    elif (seitenlaenge1 == seitenlaenge2 and seitenlaenge3 != seitenlaenge1) or+\
    (seitenlaenge2 == seitenlaenge3 and seitenlaenge1 != seitenlaenge2) or +\
    (seitenlaenge1 == seitenlaenge3 and seitenlaenge2 != seitenlaenge1):
        print("Gleichschenklige Dreiecke")
    elif seitenlaenge1 == seitenlaenge2 == seitenlaenge3:
        print("Gleichseitige Dreiecke")
    elif (seitenlaenge1 != seitenlaenge2 != seitenlaenge3):
        print("Unregelmäßige Dreiecke")

WattNDreiEck(int(input()), int(input()), int(input()))
