#! /usr/bin/env python
# -*- coding: utf-8 -*-

def BubbleSort(ZahlenLst):

    indexCounter = 0
    getauscht = False
    fertig = False

    while True:

        print(indexCounter)

        if getauscht == True and fertig == True:
            print("Fertig")
            return False
        elif ZahlenLst[indexCounter] < ZahlenLst[indexCounter+1]:
            print("In if 1")
            print(ZahlenLst[indexCounter], ZahlenLst[indexCounter+1])
            print(ZahlenLst)
            indexCounter += 1
            getauscht = False
            if fertig == False:
                fertig = True

        elif ZahlenLst[indexCounter] > ZahlenLst[indexCounter+1] and fertig == False:
            print("In if 2")
            print(ZahlenLst[indexCounter], ZahlenLst[indexCounter+1])
            print(ZahlenLst)
            ZahlenLst.insert(indexCounter, ZahlenLst.pop(indexCounter+1))
            print(ZahlenLst)
            indexCounter = 0
            getauscht = True
            if fertig == True:
                fertig = False



    print(ZahlenLst)
    return ZahlenLst

BubbleSort([1,3,6,2,8,4])
