# -*- coding: utf-8 -*-
"""
Created on Thu Mar 24 08:53:12 2022

@author: krish
"""

a=int(input())
b=int(input())
for i in range (a,b,10):
    print(i)
    if(i%2==0):
        print("Even ")
    else:
        print("odd")