from random import randint

def tspf(i, j, F, D):
    if F[i][j] != float('inf'):
        return F[i][j]
    if i == j-1:
        mini = float('inf')
        for k in range(j-1):
            mini = min(mini, tspf(k, j-1, F, D) + D[k][j])
        F[j-1][j] = mini
    else:
        F[i][j] = tspf(i, j-1, F, D) + D[j-1][j]
    return F[i][j]

n = 4
F = [[float('inf') for _ in range(n)] for _ in range(n)]
D = [[randint(1,100) for _ in range(n)] for _ in range(n)]
F[0][1] = D[0][1]

mini = float('inf')
for i in range(n-1):
    mini = min(mini, tspf(i, n-1, F, D) + D[i][n-1])

print(mini)