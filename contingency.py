import math
import itertools

def contingencyTest(data):
    n = len(data)
    r = []
    c = []

    for i in range(n):
        if data[i][0] not in r:
            r.append(data[i][0])
        if data[i][1] not in c:
            c.append(data[i][1])

    rN = len(r)
    cN = len(c)

    df = (rN-1)*(cN-1)

    rP = [0]*rN
    cP = [0]*cN

    oij = []
    for i in range(rN):
        oij.append([0]*cN)

    for i in range(rN):
        rCount = 0
        lim = 0
        for j in range(cN):
            cCount = 0
            for k in range(n):

                if lim < n:
                    if data[k][0] == r[i]:
                        rCount += 1
                    lim += 1

                if data[k][1] == c[j]:
                    cCount += 1

                if data[k][0] == r[i] and data[k][1] == c[j]:
                    oij[i][j] += 1

            cP[j] = cCount/n
        rP[i] = rCount/n

    t = 0

    for i in range(rN):
        for j in range(cN):
            t += ((oij[i][j] - n*rP[i]*cP[j])**2)/(n*rP[i]*cP[j])

    return (t, df)

data = [[0, 0],[1, 1],[0, 2],[1, 3],[0, 0],[1, 1],[0, 2],[1, 3],[0, 0],[1, 1],[0, 2],[1, 3],[0, 0],[1, 1],[0, 2],[1, 3],[0, 0],[1, 1],[0, 2],[1, 3]]
print(contingencyTest(data))
