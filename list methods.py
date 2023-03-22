# -*- coding: utf-8 -*-
"""
Created on Tue Apr  5 13:43:35 2022

@author: krish
"""

l1=[]
for i in range (1,101):
    l1.append(i**2)
print(l1) 

l1=[i**3 for i in range(1,101)]
print(l1)  