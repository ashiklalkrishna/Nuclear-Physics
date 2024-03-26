#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Sep  4 20:51:46 2023

@author: ash
"""

import numpy as np
import matplotlib.pyplot as plt
from fractions import Fraction
import sys
plt.figure(figsize=(7,20))

hw=1
D=-0.0225*hw
C=-0.1*hw

def harmonic_en(N):
    h=(N+(3/2))*hw
    return h
def centrifugal_en(l):
    c=D*l*(l+1)
    return c
def spinorbital_en(l,s):
    if s==(1/2):
        so=C*(l/2)
    if s==(-1/2):
        so=C*(-(l+1)/2)
    return so
def lval(N):
    if N%2==0:
        lvalue=np.arange(0,N+1,2)
    if N%2==1:
        lvalue=np.arange(1,N+1,2)
    return lvalue
def j(l,s):
    ls=abs(int(2*(l+s)))
    return Fraction(ls,2)
def n_r(N,l):
    return int((N-l+2)/2)

N=np.arange(0,6,1)
Lsymb=['s','p','d','f','g','h']
S=[1/2,-1/2]

for n in N:
    ehar=harmonic_en(n) 
    plt.hlines(ehar,xmin=1.2,xmax=1.7, color='black')
    plt.text(1.35,ehar+0.02, f'N={n}')
    
    L=lval(n)
    for l in L:
        ecentri=harmonic_en(n)+centrifugal_en(l)
        plt.hlines(ecentri,xmin=2.1,xmax=2.6, color='black')
        nr=n_r(n,l)
        plt.text(2.3,ecentri+0.02, f'{nr}{Lsymb[l]}')
        
        if l!=0:
            for s in S:
                espinorb=harmonic_en(n)+centrifugal_en(l)+spinorbital_en(l,s)
                plt.hlines(espinorb,xmin=3.1,xmax=3.6, color='black')
                jvalue=j(l,s)
                plt.text(2.9,espinorb, f'{nr}{Lsymb[l]}{jvalue}')
        elif l==0:
            s=1/2
            espinorb=harmonic_en(n)+centrifugal_en(l)+spinorbital_en(l,s)
            plt.hlines(espinorb,xmin=3.1,xmax=3.6, color='black')
            jvalue=j(l,s)
            plt.text(2.9,espinorb, f'{nr}{Lsymb[l]}{jvalue}')
            
plt.text(1.27, 1.35, f'(N+3/2)\u210F\u03C9')
plt.text(2.25, 1.35, f'Dl(l+1)')
plt.text(3.25, 1.35, f'C l\u22C5s')

plt.ylabel('Energy (in terms of \u210F\u03C9)')
plt.gca().axes.get_xaxis().set_visible(False)
plt.title('Energy level scheme for nuclear shell model')
plt.tight_layout()
plt.show()
    