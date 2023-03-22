# -*- coding: utf-8 -*-
"""
Created on Wed Apr 13 10:06:42 2022

@author: krish
"""

n=int(input())
l1=[int(i) for i in input().split()][:n]
print(l1)
print(l1.index(max(l1)))