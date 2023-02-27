from random import randint

def tsp(S, t):

    S.remove(t)

    if len(S) == 1:
        return d[0][t]
    
    mini = float('inf')
    for r in range(1, len(S)):
        mini = min(mini, tsp(S.copy(), S[r]) + d[S[r]][t])
    
    return mini


n = 4
C = [i for i in range(n)]
d = [[randint(1,100) for _ in range(n)] for _ in range(n)]

print(C)
for row in d:
    print(row)

mini = float('inf')
for r in range(1, n):
    mini = min(mini, tsp(C.copy(), r) + d[r][0])

print(mini)