#! /usr/bin/env python
# -*- coding: utf-8 -*-

def Fibonacci(ende):
    """Gibt die Fibonacci-Zahlenfolge bis zum eingegeben Endwert wieder."""

    a = 0
    b = 1
    c = 0

    print(a)
    print(b)

    for i in range(ende):
        c = a + b
        if c >= ende:
            return
        else:
            print(c)
            a = b
            b = c
    return(Fibonacci(ende))

Fibonacci(int(input("Gib ein wie weit die Fibonacci-Zahl gehen soll: ")))
