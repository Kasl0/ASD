#Kacper Słoniec
#Złożoność O(n^2)
#Opis: Program niestety znajduje tylko przystanki, na których Marian przejmuje kierownicę (nie znajduje przesiadek Marian -> Jacek).
from time import sleep
from kol2atesty import runtests

def drivers(P, B):
    PP = [(P[i][0], P[i][1], i) for i in range(len(P))]
    PP.sort()
    F = [[[-1, []] for _ in range(B)] for _ in range(4)]
    F[0][0][0] = 0
    stops = 0
    controls = 0
    last_order = -1

    for point in PP:
        cord, type, order = point
        if type == False: #punkt kontrolny
            controls += 1
        if type == True: #punkt przesiadkowy
            if stops == 0:
                F[1][1][0] = 0
            else:
                for i in range(4):
                    if F[i][stops][0] != -1:

                        if F[0][stops+1][0] != -1:
                            if F[i][stops][0] + controls < F[0][stops+1][0]:
                                F[0][stops+1][0] = F[i][stops][0] + controls
                                Temp = F[i][stops][1].copy()
                                if i != 0: Temp.append(last_order)
                                F[0][stops+1][1] = Temp
                        else:
                            F[0][stops+1][0] = F[i][stops][0] + controls
                            Temp = F[i][stops][1].copy()
                            if i != 0: Temp.append(last_order)
                            F[0][stops+1][1] = Temp

                        if i+1 < 4:
                            if F[i+1][stops+1][0] != -1:
                                if F[i][stops][0] < F[i+1][stops+1][0]:
                                    F[i+1][stops+1][0] = F[i][stops][0]
                                    F[i+1][stops+1][1] = F[i][stops][1].copy()
                                    if i == 0:
                                        F[i+1][stops+1][1].append(last_order)
                            else:
                                F[i+1][stops+1][0] = F[i][stops][0]
                                F[i+1][stops+1][1] = F[i][stops][1].copy()
                                if i == 0:
                                    F[i+1][stops+1][1].append(last_order)
            last_order = order
            controls = 0
            stops += 1

    mini = float('inf')
    Temp = []
    for i in range(4):
        if F[i][stops][0] < mini:
            mini = F[i][stops][0]
            Temp = F[i][stops][1]

    """for i in range(4):
        for j in range(9):
            print(F[i][j], end='')
        print()"""

    return Temp

# zmien all_tests na True zeby uruchomic wszystkie testy
runtests( drivers, all_tests = True )