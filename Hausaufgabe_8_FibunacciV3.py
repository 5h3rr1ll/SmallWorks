#! /usr/bin/env python
# -*- coding: utf-8 -*-

def Fibo(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        print(n)
        return Fibo(n-1) + Fibo(n-2)

print(Fibo(int(input("Die Summe nach dem wievielten Wachstumszyklus möchtest du wissen? "))))
