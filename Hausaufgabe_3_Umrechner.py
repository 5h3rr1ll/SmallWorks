#! /usr/bin/env python
# -*- coding: utf-8 -*-

def UnwandlerDeziBinaer(n):
    """Diese Funktion rechnet einem entweder eine Dezimalzahl in eine Binärzahl
    um oder eine Binärzahl in eine Dezimalzahl. Am Anfang erscheint ein Menü-
    Abfrage, dort einafach nur 1 oder 2 eingeben und die Eingabe mit Enter bestätigen.
    Danach die Zahl eingeben und mit Enter bestätigen, die umgerechnet werden soll."""
    if n == "1":
        n = input("Welche Zahl soll in eine Binärzahl umgewandelt werden? ")
        n = bin(int(n)) #Da die Eingabe ein String ist, bin() jedoch eine integer benötigt, muss int() genutzt werden
        #bin() rechnet Dezimalzahlen in Binär um
    else:
        n = input("Welche Zahl soll in eine Dezimalzahl umgewandelt werden? ")
        n = int(n,2) # in
    print(n)

UnwandlerDeziBinaer(input("Was möchtest du Umwanden?Gib 1 für Dezimalzahl 2 für eine BinaerZahl: "))
