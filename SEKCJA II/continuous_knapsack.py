from random import randint

def f(V, P, b):
    val = 0
    n = len(V)

    while n > 0:
        maks = P[0]/V[0]
        maks_index = 0
        for i in range(1, n):
            if P[i]/V[i] > maks:
                maks = P[i]/V[i]
                maks_index = i

        if b-V[maks_index] <= 0:
            return val + b/V[maks_index]*P[maks_index]
    
        b -= V[maks_index]
        val += P[maks_index]
        n -= 1
        V.pop(maks_index)
        P.pop(maks_index)
    
    return val

n = 5
V = [randint(1,100) for _ in range(n)]
P = [randint(1,100) for _ in range(n)]
b = 150

print(V)
print(P)
print(f(V, P, b))