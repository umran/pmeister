import math
import itertools

def pWilcoxonRankSum(setA, setB, alt=None):
    if alt is None:
        alt = "et"

    setMerged = setA + setB
    setMerged.sort()
    nA = len(setA)
    nB = len(setB)
    nT = len(setMerged)
    allCombinations = nCk(nT, nA)
    ranks = []
    wA = 0
    count = 1

    for i in range(nT):
        if(i>0 and setMerged[i] == setMerged[i-1]):
            count += 1
            rank = sum(range(i+2-count, i+2))/count
            ranks.append(rank)

            for j in range(count):
                ranks[i-j] = rank
        else:
            count = 1
            ranks.append(i+1)

    for i in range(nA):
        for j in range(nT):
            if setA[i] == setMerged[j]:
                wA += ranks[j]
                break

    ## enumerate all possible ways of getting wA as or more extreme than recorded wA
    critical = criticalCombinations(ranks, wA, nA, alt)
    p = critical/allCombinations

    if alt == "et":
        if p > 0.5:
            p = 2*(1-p)
        else:
            p = 2*p
    return p

def criticalCombinations(ranks, wA, nA, alt):
    count = 0
    combinations = itertools.combinations(ranks, nA)
    for comb in combinations:
        sum = 0
        for i in range(len(comb)):
            sum += comb[i]

        if alt == "gt" or alt == "et":
            if sum >= wA:
                count += 1
        elif alt == "lt":
            if sum <= wA:
                count += 1
    return count

def nCk(n,k):
    return math.factorial(n)/(math.factorial(n-k)*math.factorial(k))
