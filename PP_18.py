# -*- coding: utf-8 -*-
"""
Created on Wed Mar 23 09:20:31 2022

@author: krish
"""

sum=0
a=int(input())
while(a!=0):
    temp=((a%10)**3)
    sum=sum+temp
    a=a//10
print(sum)
if(sum==a):
    print("Amstrong")
else:
    print("Not a amstrong")