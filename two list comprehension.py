# -*- coding: utf-8 -*-
"""
Created on Wed Apr 13 09:22:01 2022

@author: krish
"""
m=int(input())
n=int(input())
l1=[int(x) for x in input().split()][:m]
l2=[int(y) for y in input().split()][:n]
l3=[int(x) for x in l1 if x%2 !=0]
l4=[int(y) for y in l2 if y%2 ==0]
print(l3+l4)
