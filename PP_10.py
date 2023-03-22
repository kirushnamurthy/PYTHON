# -*- coding: utf-8 -*-
"""
Created on Tue Mar 15 15:28:43 2022

@author: krish
"""

x=int(input("value of x "))
y=int(input("value of y "))
z=int(input("value of z "))
if (x>y and x>z):
    print(x,"is the largest of ",y,"and",z)
elif( y>z):
    print(y,"is the largest of ",x,"and",z)    
else:
    print(z,"is the largest of",x,"and",y)        