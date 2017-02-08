#! /usr/bin/env python
# -*- coding: utf-8 -*-

def BubbleSort(ZahlenLst):

    start = 0

    for i in range(start, len(ZahlenLst)+1):
        if ZahlenLst[start] < ZahlenLst[start+1]:
            start += 1

        else:
            ZahlenLst.insert(start, ZahlenLst.pop(start+1))
            start = 0
            continue


    print(ZahlenLst)

BubbleSort([9,5,3,1,8,4])
