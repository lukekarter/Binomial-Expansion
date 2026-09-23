# Binomial Expansion Machine

# Import modules

import math
from sympy import *

# Subprograms

def pascalTriangle(pBinomial, pExponent): # return a list with the pascal triangle row for the given exponent
    pascalRow = []
    for i in range(0, pExponent):
        value = math.factorial(pExponent) / (math.factorial(i) * math.factorial(pBinomial))
        pascalRow.append(value)
    print(pascalRow)
    return pascalRow

def binomialExpansion(pBinomial,pExponent):
    coefficients = pascalTriangle(pBinomial, pExponent)
    return expandedBinomial

# Main program

firstVar = symbols(input("Enter first variable name: "))
if input("Do you have a second algebraic term? Y/N: ").lower() == "y":
 secondVar = symbols(input("Enter second variable name: "))
binomial = int(input("Enter binomial expression: "))
exponent = int(input("Enter the exponent of the binomial: "))
binomialExpansion(binomial,exponent)
print(expandedBinomial)