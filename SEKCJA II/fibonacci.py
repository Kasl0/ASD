def fib(n):
    if n <=2: return 1
    return fib(n-1) + fib(n-2)

def fib_dyn(n):
    F = [1] * (n+2)
    for i in range(2, n+1): F[i] = F[i-1] + F[i-2]
    return F[n]

def fib_dyn2(n):
    if n <= 1: return 1
    Fi1 = 1
    Fi2 = 1
    for i in range(2, n+1):
        Fi = Fi1 + Fi2
        Fi2 = Fi1
        Fi1 = Fi
    return Fi