# -*- coding: utf-8 -*-
"""
Created on Wed Mar 23 09:33:01 2022

@author: krish
"""

dec=int(input())
binary=0
i=0
while(i>=0):
    rem=dec%10
    binary=binary+rem*(10**i)
    dec=dec//10
print(binary)    