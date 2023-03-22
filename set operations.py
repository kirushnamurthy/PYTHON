# -*- coding: utf-8 -*-
"""
Created on Thu Apr 21 08:53:10 2022

@author: krish
"""

#a={1,2,3,4,5}
#print(4 not in a)

#a={1,2,3,4,4}
#b={1,2,3,4,5}
#print(a.issuperset(b) )
#print(a<=b)

#a={1,2,3,4,5}
#print(a.copy())

#a=1,2,3,4,5
#for i in enumerate(a):
    #print(set(i))
#print(set(enumerate(a))) another print form

#a={1,2,3,4,6}
#b={1,2,3,4,5}
#print(a!=b)

#a=[1,2,3,4]
#print(set(a))

b=set()
a={1,2,3,4,5,4,4}
for i in a :
    if(i==4):
        b.add(i)
        print(b)

