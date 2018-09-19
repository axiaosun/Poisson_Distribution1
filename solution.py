#!/usr/bin/env python3

import math
from math import e

def factor (num):
    fact = 1
    if num != 0:
        for i in range (1, num + 1):
            fact *= i
    return fact

def poiss (lambda_, k_):
    return ((lambda_**k_)*(e**(-k_))) / (factor(k_))

lambda_ = float(input())
k_ = int(input())

result = poiss(lambda_, k_)

print(round(result, 3))
