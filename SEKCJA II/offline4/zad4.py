#Kacper Słoniec

#Opis algorytmu:
#Sprawdzamy rekurencyjnie każdy z każdym.

#Złożoność czasowa: O(2^n)

from zad4testy import runtests

def students_number(T):
    return (T[0] * (T[2]-T[1]))

def check_separate(T, F, i):
    h, a, b, w = T[i]
    for index in F:
        if not (T[index][2] < a or T[index][1] > b):
            return False
    return True

def f(T, i, b, F):
    if i == 0 and T[0][3] <= b and check_separate(T, F, 0):
        F.append(0)
        return ((T[0][0] * (T[0][2]-T[0][1])), F)
    elif i == 0:
        return (0, F)

    if b-T[i][3] >= 0 and check_separate(T, F, i):
        FF = F.copy()
        FF.append(i)
        a, aF = f(T, i-1, b, F)
        b, bF = f(T, i-1, b-T[i][3], FF)
        b += (T[i][0] * (T[i][2]-T[i][1]))
        if a > b:
            return (a, aF)
        else:
            return (b, bF)
    else:
        return f(T, i-1, b, F)

def select_buildings(T, p):
    n = len(T)
    students, buildings = f(T, n-1, p, [])
    buildings.sort()
    return buildings

    """F = [[(0, []) for _ in range(p+1)] for _ in range(n)]
    for b in range(T[0][3], p+1): F[0][b] = (students_number(T[0]), [0])
    for b in range(p+1):
        for i in range(1, n):
            F[i][b] = F[i-1][b]
            if b-T[i][3] >= 0:
                if check_separate(T, F[i-1][b-T[i][3]][1], i):
                    if F[i-1][b-T[i][3]][0] + students_number(T[i]) > F[i][b][0]:
                        Temp = F[i-1][b-T[i][3]][1].copy()
                        Temp.append(i)
                        F[i][b] = (F[i-1][b-T[i][3]][0] + students_number(T[i]), Temp)
                else:
                    #stać nas na budynek, ale koliduje z pozostałymi
                    #F[i-1][b-T[i][3]][1] - budynki
                    #T[i] - nasz budynek
                    Temp = F[i-1][b-T[i][3]][1].copy()
                    val = F[i-1][b-T[i][3]][0]

                    h, a, bb, w = T[i]
                    for index in Temp:
                        if not (T[index][2] < a or T[index][1] > bb):
                            #koliduje => wywal
                            Temp.remove(index)
                            val -= students_number(T[index])
                    
                    if val + students_number(T[i]) > F[i][b][0]:
                        Temp.append(i)
                        F[i][b] = (val + students_number(T[i]), Temp)



    for wiersz in F:
        print(wiersz)

    sleep(1000000)
                    
    return sorted(F[n-1][p][1])"""

T = [ (2, 1, 5, 3),
(3, 7, 9, 2),
(2, 8, 11, 1) ]
p = 5
#print(select_buildings(T, p))
runtests( select_buildings )