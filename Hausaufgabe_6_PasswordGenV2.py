#! /usr/bin/env python
# -*- coding: utf-8 -*-

from random import *
from string import *

max_lenght = 8
Zahlen = 0,1,2,3,4,5,6,7,8,9

s = []

def PwGen():
    """Generiert beim ausführen ein Passwort dass aus 2 Große-Buchstaben, 2 Klein
    -Buchstaben, 2 Zaheln und 2 Sonderzeichen besteht."""

    for i in range(1, (max_lenght/4)+1):
        s.append(choice(ascii_uppercase))
        s.append(str(choice(Zahlen)))
        s.append(choice(ascii_lowercase))
        s.append(choice(punctuation))

    shuffle(s)
    print("".join(s))

PwGen()
