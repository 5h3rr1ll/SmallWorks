#! /usr/bin/env python
# -*- coding: utf-8 -*-

def LaenderDic():
    """In diese Fuktion können die Englische Namen von Ländern eingegebne werden
    und werden, sofern vorhanden, auf Deutsch wiedergegben. Wenn nicht vorhanden
    scheint eine dementsprechende Meldung."""

    f = open("dic.txt", "r")

    dic = {}

    for line in f:
        line = line.strip()
        Woerter = line.split(" ")

        dic[Woerter[0]] = Woerter[1]
    f.close()

    dicKeys = dic.keys()

    userInput = input("Nenne den englischen Namen eines Landes: ")

    if userInput in dicKeys:
        print(dic[userInput])
    else:
        print("Sorry, das Land ist nicht im Wörterbuch.")

LaenderDic()
