#Głodna żaba
#minimalna liczba skoków

def zaba(T, i, j):
    if i >= len(T) - 1:
        return 0
    mini = float('inf')
    j += T[i]
    for k in range(1, j+1):
        tmp = zaba(T, i+k, j-k)
        if tmp < mini:
            mini = tmp
    return mini + 1

T = [3,0,2,1,0,2,5,0]
print(zaba(T, 0, 0))