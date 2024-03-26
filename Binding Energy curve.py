#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Jul 11 23:42:11 2023
@author: ash
"""

import numpy as np
import matplotlib.pyplot as plt
plt.figure(figsize=(10,6))

def bind_en (A):  #defining binding energy function
    avol=14.1       #initializing the coefficents 
    asurf=13
    acol=0.595
    asym=19
    
    Z=(A/2)*(1/(1+0.25*(A**(2/3))*(acol/asym)))
    Z=round(Z)
    
    if (A%2)!=0 and (Z%2)==0:
        apar=0
    elif (A%2)==0 and (Z%2)!=0:
        apar=0
    elif (A%2)==0 and (Z%2)==0:
        apar=33.5
    elif (A%2)!=0 and (Z%2)!=0:
        apar=-33.5
    
    b = avol*A-asurf*(A**(2/3))-(acol*Z*(Z-1))/(A**(1/3))-asym*((A-2*Z)**2)/A+apar/(A**(3/4))
        
    return b/A

A=np.arange(1,300,1) #defining an array for A
BE=[]

for a in A: #iterating over A and corresponding Z values
    be=bind_en(a)
    BE.append(be)
max_be=max(BE)
max_a=BE.index(max_be)

plt.plot(A, BE, color='red')
plt.scatter(4, bind_en(4), color='red')
plt.text(5, bind_en(4)+0.5, 'Helium(2,4)')
plt.scatter(56, bind_en(56), color='red')
plt.text(56, bind_en(56)-1.2, 'Iron(26,56)')
plt.scatter(12, bind_en(12), color='red')
plt.text(12, bind_en(12)-1, 'Carbon(6,12)')
plt.scatter(257, bind_en(257), color='red')
plt.text(257, bind_en(257)-1.2, 'Fermium(100,257)')
plt.scatter(max_a, max_be, color='black', label="Maximum BE per nucelon")
plt.xlabel('A')
plt.ylabel('Binidng energy per nucleon (MeV)')
plt.title('Binding energy per nucelon curve')
plt.legend(loc='lower right')
plt.grid()
plt.show()