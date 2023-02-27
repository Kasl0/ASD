#Spadające klocki

def f(T):
    A = []
    n = len(T)
    for i in range(n):
        A.append(0)
    for i in range(n):
        maximum = 1
        for j in range(i):
            if T[j][0] <= T[i][0] and T[j][1] >= T[i][1]:
                maximum = max(maximum, A[j] + 1)
            # if T[i][0] <= T[j][0] and T[i][1] >= T[j][0]:
            #     A[i] += 1
        A[i] = maximum
    print(A)
    best = 0
    for i in range(n):
        best = max(best, A[i])
    return best

print(f([[0,5], [0,2], [0,3]]))