import math

def factorial(x):
    res = 1
    for i in range(1, x):
        res *= i
    return res

def prob(n, p, r):
    res = (factorial(n+r-1)*pow(p, r)*pow(1-p, n)) / (factorial(r-1)*factorial(n))
    return res

def inforMeasure(n, p, r):
    px = prob(n, p, r)
    return 0 - math.log2(px)

def sumProb(N, p, r):
    sum = 0
    for i in range(1, N+1):
        sum += prob(i, p, r)
    return sum

def approxEntropy(N, p, r):
    sum = 0
    for i in range(1, N+1):
        sum += inforMeasure(i, p, r) * prob(i, p, r)
    return sum