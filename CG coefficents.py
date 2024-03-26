#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Sep  9 14:30:01 2023

@author: ash
"""

from sympy.physics.quantum.cg import CG

# Define the quantum numbers
j1 = 2
m1 = 2
j2 = 1
m2 = -1
J = 1
M=1

# Calculate the Clebsch-Gordan coefficient
cg_coefficient = CG(j1, m1, j2, m2, J, M)
numerical_value = cg_coefficient.doit()

print(numerical_value)