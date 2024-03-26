#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Jul 17 00:52:07 2023

@author: ash
"""

#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Jul 11 23:42:11 2023
@author: ash
"""

import numpy as np
import matplotlib.pyplot as plt
plt.figure(figsize=(10,6))
def bind_en (A):  #Defining a function to calculate binding energy 
                    #curve using semi-emperical mass formulae
    avol=14.1       #Initializing the coefficents 
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
        
    evol=avol*A
    esurf=asurf*(A**(2/3))
    ecol=(acol*Z*(Z-1))/(A**(1/3))
    easym=asym*((A-2*Z)**2)/A
    epair=apar/(A**(3/4))
    
    b=evol-esurf-ecol-easym+epair
        
    return b/A, evol/A, esurf/A, ecol/A, easym/A, epair/A

A=np.arange(1,300,1) #Defining an array ranging for A
BE=[]
VE=[]
SE=[]
CE=[]
ASE=[]
PRE=[]

for a in A: #Iterating over A and corresponding Z values
    be,ve,se,ce,ase,pre=bind_en(a)
    BE.append(be)
    VE.append(ve)
    SE.append(se)
    CE.append(ce)
    ASE.append(ase)
    PRE.append(pre)
plt.plot(A, BE, label='Binding Energy', color='red', marker='o', markevery=25)
plt.plot(A, VE, label='Volume Energy', color='orange', marker='^', markevery=25)
plt.plot(A, SE, label='Surface Energy', color='navy', marker='s', markevery=25)
plt.plot(A, CE, label='Coloumb Energy', color='blue', marker='d', markevery=25)
plt.plot(A, ASE, label='Asymmetry Energy', color='brown', marker='p', markevery=25)
plt.plot(A, PRE, label='Paring Energy', color='green', marker='*', markevery=25)

plt.xlabel('A')
plt.ylabel('Binidng energy per nucleon (MeV)')
plt.title('Binding energy curve using SEMF')
plt.legend()
plt.grid()
plt.show()