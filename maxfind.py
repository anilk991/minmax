# -*- coding: utf-8 -*-
"""
Created on Tue Aug 28 10:48:53 2018

@author: Anil Kumar Koundal

Python script find maximum value in a list.
"""

def findmax(arr):
    if(len(arr) <= 0):
        print("No list in input.")
    else:
        max_ = arr[0]
        for i in range(1,len(arr)):
            if(max_ < arr[i]):
                max_ = arr[i]
        return max_

def findmin(arr):
    if(len(arr) <= 0):
        print("No list in input.")
    else:
        min_ = arr[0]
        for i in range(1,len(arr)):
            if(min_ > arr[i]):
                min_ = arr[i]
        return min_


num=[0,34,32,21,23,100]
print(findmax(num))
print(findmin(num))