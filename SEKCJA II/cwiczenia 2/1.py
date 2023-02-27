#Wycinka lasu

def fun(T, n):
    max(T[n] + fun(T, n-2), T[n-1] + fun(T,n-3))

def las(T,n):
    if n < 0:
        return 0 
    return max(las(T,n-2)+T[n],las(T,n-1))

def las_iteracyjnie(T):
    pom = [0 for i in range(len(T))]
    for i in range(len(T)):
        if i > 2:
            pom[i] = T[i] + max(pom[i-2],pom[i-3])
        else:
            pom[i] = T[i]
    return max(pom[len(T)-1],pom[len(T)-2])

print(las_iteracyjnie([5,1,2,7,4,2]))