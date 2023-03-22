# -*- coding: utf-8 -*-
"""
Created on Thu Mar 17 09:45:33 2022

@author: krish
"""
sum=0
a=int(input())
while(a!=0):
    sum=sum+(a%10)
    a=a//10
print(sum)

