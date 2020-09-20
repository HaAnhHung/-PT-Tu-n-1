import math

def prob(n, p):
    return p*pow(1-p, n-1)

def inforMeasure(n, p):
    px = prob(n, p)
    return 0 - math.log2(px)

def sumProb(N, p):
    sum = 0
    for i in range(1, N+1):
        sum += prob(i, p)
    return sum

def approxEntropy(N, p):
    sum = 0
    for i in range(1, N+1):
        sum += inforMeasure(i, p) * prob(i, p)
    return sum