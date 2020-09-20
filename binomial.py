import math
import operator as op
from functools import reduce


def ncr(n, r):
    r = min(r, n - r)
    number: float = reduce(op.mul, range(n, n - r, -1), 1)
    denom: float = reduce(op.mul, range(1, r + 1), 1)
    return number // denom


def prob(n, p, N):
    return float(ncr(N, n) * pow(p, n) * pow(1 - p, N - n))


def infoMeasure(n, p, N):
    return 0 - math.log2(prob(n, p, N))


def sumProb(p, N):
    '''
    sumProb(15, 0.5) = 0.999969482421875
    sumProb(30, 0.5) = 0.9999999990686774
    => Hàm sumProb có thể sử dụng để kiểm chứng tổng xác suất của phân bố binamial = 1 
    '''
    sum: float = 0
    for x in range(1, N + 1):
        sum += prob(x, p, N)
    return sum

def approxEntropy(p, N):
    '''
        Ham approxEntropy tinh xap xi entropy cua nguon tin binomial, duoc tinh bang tong cua cac xac suat nhan voi luong thong
        tin tuong ung.
        approxEntropy(0.5, 2) = 1.0
        approxEntropy(0.5, 5) = 2.041942411043098
        approxEntropy(0.5, 100) = 4.369011409223017
    '''
    sum: float = 0
    for x in range(1, N + 1):
        sum += infoMeasure(x, p, N) * prob(x, p, N)
    return sum

