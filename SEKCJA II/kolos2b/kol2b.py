from kol2btesty import runtests

def min_cost(O, C, T, L):
    n = len(O)
    P = [(O[i], C[i]) for i in range(n)]
    P.sort()
    
    F = [[float('inf') for j in range(T)] for i in range(n+1)] # tablica T x n+1: koszt, przejechane km
    FB = [[float('inf') for j in range(T)] for i in range(n+1)] # tablica T x n+1 dla bonusa: koszt, przejechane km

    F[0][0] = 0

    for i in range(n):
        if i == 0: next_distance = P[i][0]
        else: next_distance = P[i][0] - P[i-1][0]

        for j in range(T):
            if F[i][j] != float('inf'):

                if next_distance <= T - j:
                    F[i+1][0] = min(F[i+1][0], F[i][j] + P[i][1])

                if next_distance < T - j:
                    F[i+1][j+next_distance] = min(F[i+1][j+next_distance], F[i][j])

                else: #bonus odpalamy gdy: T < next_distance + j <= 2T
                    if next_distance <= 2*T - j:
                        FB[i+1][0] = min(FB[i+1][0], F[i][j] + P[i][1])

                    if next_distance < 2*T - j:
                        FB[i+1][j+next_distance-T] = min(FB[i+1][j+next_distance-T], F[i][j])
            
            if FB[i][j] != float('inf'):

                if next_distance <= T - j:
                    FB[i+1][0] = min(FB[i+1][0], FB[i][j] + P[i][1])

                if next_distance < T - j:
                    FB[i+1][j+next_distance] = min(FB[i+1][j+next_distance], FB[i][j])

    mini = min(F[n][0] - P[n-1][1], FB[n][0] - P[n-1][1])
    for j in range(1, T):
        mini = min(mini, F[n][j], FB[n][j])

    return mini           

# zmien all_tests na True zeby uruchomic wszystkie testy
runtests( min_cost, all_tests = False )
