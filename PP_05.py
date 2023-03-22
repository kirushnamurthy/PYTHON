# -*- coding: utf-8 -*-
"""
Created on Tue Mar 15 14:26:11 2022

@author: krish
"""

x=int(input('ENTER YOUR AGE'))
if(x>18):
    print("ELIGIBLE")
else:
    x=18-x
    print(x)
    print("not eligible")    