#! /usr/bin/env python
# -*- coding: utf-8 -*-

def Fibonacci(ende):
    """Gibt die Fibonacci-Zahlenfolge bis zum eingegeben Endwert wieder."""

    a, b = 0, 1

    for i in range(ende):
# Im print() das 'end = " "' bezweckt, dass am Ende der print-Anweisung kein \n
# steht und somit in eine neue Zeile geprintet wird. end="Platzhalter", im Platz-
# halter kann bestimmt werden, wie die einzielnen ausgeprinteten Objekte vonein-
# ander getrennt sein sollen. In meinem Fall mit einem Leerzeichen, könnte aber
# auch ein belibiges anderes Zeichen sein.
        print(a, end=" ")
# Um für die Fibonacci-Folge die Werte durchwandern zu lassen funktioniert in
# Python folgende Syntax:
        a, b = b, a + b
        if a >= ende:
            print("\n")
            return
    return(Fibonacci())

Fibonacci(int(input("\n Gib ein wie weit die Fibonacci-Zahl gehen soll: ")))
