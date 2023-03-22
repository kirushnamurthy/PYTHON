# -*- coding: utf-8 -*-
"""
Created on Thu Mar 17 09:11:03 2022

@author: krish
"""
n=p=z=0
while(1):
    num=int(input())
    if(num==-1):
        break
    elif(num==0):
        z=z+1
    elif(num>0):
        p=p+1
    else:
        n=n+1
print("no of positive",p)        
print("no of negatives",n)     
print("no of zeros",z)    