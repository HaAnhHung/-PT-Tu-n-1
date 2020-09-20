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


def sumProb(n, p, N):
    sum: float = 0
    for x in range(n, N + 1):
        sum += prob(x, p, N)
    return sum


def approxEntropy(n, p, N):
    sum: float = 0
    for x in range(n, N + 1):
        sum += infoMeasure(x, p, N) * prob(x, p, N)
    return sum
