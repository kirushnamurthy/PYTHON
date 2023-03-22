# -*- coding: utf-8 -*-
"""
Created on Thu Mar 17 09:25:41 2022

@author: krish
"""

n=p=z=sum=sum1=0
while(1):
    num=int(input())
    if(num==-1):
        break
    elif(num==0):
        z=z+1
    elif(num>0):
        p=p+1
        sum=sum+num
    else:
        n=n+1
        sum1=sum1+num
print("no of positive",p)
print("sum",sum)       
print("no of negatives",n)  
print("sum1",sum1)   
print("no of zeros",z)    