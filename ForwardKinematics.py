# -*- coding: utf-8 -*-
"""
Created on Mon Oct 14 17:42:01 2024

@author: apark
"""

import numpy as np
from sympy import *
from scipy.linalg import expm
from ModernRobotics import *

#Creating all necessary symbols
h, L1, L2, L3, L4, L5, L6, theta1, theta2, theta3, theta4, theta5, theta6 = symbols('h, L1, L2, L3, L4, L5, L6, theta1, theta2, theta3, theta4, theta5, theta6')

w1 = np.array([0,0,1])
w2 = np.array([1,0,0])
w3 = np.array([-1,0,0])
w4 = np.array([1,0,0])
w5 = np.array([0,-1,0])
w6 = np.array([1,0,0])

q1 = np.array([0,0,0])
q2 = np.array([0,-L1,h])
q3 = np.array([0,-L1-L2,h])
q4 = np.array([0,-(L1+L2+L3),h])
q5 = np.array([L4,-(L1+L2+L3),h])
q6 = np.array([L4,-(L1+L2+L3+L5),h])

v1 = np.cross(q1,w1)
v2 = np.cross(q2,w2)
v3 = np.cross(q3,w3)
v4 = np.cross(q4,w4)
v5 = np.cross(q5,w5)
v6 = np.cross(q6,w6)

S1 = np.concatenate((w1, v1))
S2 = np.concatenate((w2, v2))
S3 = np.concatenate((w3, v3))
S4 = np.concatenate((w4, v4))
S5 = np.concatenate((w5, v5))
S6 = np.concatenate((w6, v6))

S = np.array([S1, S2, S3, S4, S5, S6]).T

Sb1 = Matrix(VecTose3(S1))
Sb2 = VecTose3(S2)
Sb3 = VecTose3(S3)
Sb4 = VecTose3(S4)
Sb5 = VecTose3(S5)
Sb6 = VecTose3(S6)

P1, D1 = Sb1.diagonalize()

ed1 = Matrix([exp()])
"""
e1 = simplify(exp(Sb1*theta1))
e2 = simplify(exp(Sb2*theta2))
e3 = simplify(exp(Sb3*theta3))
e4 = simplify(exp(Sb4*theta4))
e5 = simplify(exp(Sb5*theta5))
e6 = simplify(exp(Sb6*theta6))
"""
#T01 = e1 @ e2 @ e3 @ e4 @ e5 @ e6 @ M
#print(T01)