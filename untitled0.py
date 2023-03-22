# -*- coding: utf-8 -*-
"""
Created on Fri Aug 12 10:52:34 2022

@author: krish
"""

class array:
   
    def read(self,a):
       l1=[]
       for i in range(0,a):
           k=int(input())
           l1.append(int(k))
       for i in l1:
           print(i,end=" ")
       
a=int(input()) 
obj=array()
obj.read(a)
   
    
    