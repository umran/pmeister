import math

def pBinomial(t, n, p, alt=None):
    if alt is None:
        alt = "et"

    phi = phiBinomial(t, n, p)

    if alt == "lt":
        return phi
    elif alt == "gt":
        return 1-phi
    elif alt == "et":
        if(phi > 0.5):
            return 2*(1-phi)
        else:
            return 2*phi


def phiBinomial(k, n, p):
    phi = 0
    for i in range(k+1):
        phi += nCk(n,i)*p**(i)*(1-p)**(n-i)

    return phi

def nCk(n,k):
    return math.factorial(n)/(math.factorial(n-k)*math.factorial(k))
