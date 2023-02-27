#Ładowanie promu

def prom(T,d):
    for i in range(len(T)):
        if fun(T,i,d,d) is False:
            max = i
            break
    return max

def fun(T,i,L,R):
    if L< 0 or R < 0 :
        return False
    elif i < 0:
      return True
    else: return fun(T,i-1,L-T[i], R) or fun(T,i-1,L,R-T[i])

print(prom([1,3,5,2,6,4,2], 5))