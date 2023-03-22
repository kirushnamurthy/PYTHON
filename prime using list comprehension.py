# -*- coding: utf-8 -*-
"""
Created on Wed Apr 13 10:28:30 2022

@author: krish
"""

l1=[x for x in range(1,101) if all (x%y!=0 for y in range (2,x))]
print(l1)