import math
import random

def sim(k, array, nSamples):
    n = len(array)
    kUnique = 0
    for i in range(nSamples):
        sample = []
        countUnique = 0

        for j in range(k):
            sample.append(random.choice(array))

        for l in range(n):
            count = 0
            for m in range(k):
                if array[l] == sample[m]:
                    count += 1
            if count == 1:
                countUnique += 1

        if countUnique == k:
            kUnique += 1

    prob = float(kUnique)/float(nSamples)
    print(prob)

def sim2(k, array, nSamples):
    n = len(array)
    kUnique = 0
    for i in range(nSamples):
        sample = []
        countUnique = 0

        for j in range(n):
            sample.append(random.choice(array))

        for l in range(n):
            count = 0
            for m in range(n):
                if array[l] == sample[m]:
                    count += 1
            if count == 1:
                countUnique += 1

        if countUnique == k:
            kUnique += 1

    prob = float(kUnique)/float(nSamples)
    print(prob)

a = []

for i in range(100):
    a.append(i+1)

sim(25, a, 10000)
sim2(25, a, 10000)
