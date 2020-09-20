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
    '''
        Ham approxEntropy tinh xap xi entropy cua nguon tin geometric, duoc tinh bang tong cua cac xac suat nhan voi luong thong
        tin tuong ung.
        approxEntropy(3, 0.5) = 1.375
        approxEntropy(6, 0.5) = 1.875
        approxEntropy(50, 0.5) = 1.9999999999999538
    '''
    sum = 0
    for i in range(1, N+1):
        sum += inforMeasure(i, p) * prob(i, p)
    return sum