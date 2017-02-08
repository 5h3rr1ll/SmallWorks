#! /usr/bin/env python
# -*- coding: utf-8 -*-

def Schachbrett(n):
    korn = 1
    for x in range(64):
        korn *= 2
    print(korn)


Schachbrett(64)
