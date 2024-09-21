#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import random
a=1
b=99
hads = random.randint(a,b)
print(hads)
javab = input()
while javab != 'd':
    if javab =='k':
        b=hads
        hads = random.randint(a,b)
        print(hads)
        javab = input()
        if javab =='b':
            a=hads
            hads = random.randint(a,b)
            print(hads)
            javab = input()
            print('woooow,Idid it')

