# -*- coding: utf-8 -*-
"""
Created on Thu May 19 14:25:54 2022

@author: krish
"""

import re
a="krish"
b="k"
if re.match(b,a):
    print("found")
else:
    print("not found")
    
    
    
a="krish"
b="r"
if re.search(b,a):
    print("found")
else:
    print("not found")   
    
    
a="iam a good boy"
b="good"
c= re.sub(b,"BAD",a)
print(c)


a="krsh is studying is"
b="is"
c=re.findall(b,a)
print(c)
    
a="krsh is studying is"
b="is"
c=re.finfiter(b,a)
print(c)
    