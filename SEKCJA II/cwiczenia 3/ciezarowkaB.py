def ciezarowkb(T,L):
    p = 0
    i = 0
    while(p<len(T)):
        cost = T[i][0]
        j = i+1
        mincost = T[j][0]
        flag = False
        while(T[j][0]-T[i][0]<L and j < len(T)):
            if T[j][1] < cost:
                flag = True
                break
            if T[j][0]<mincost:
                mincost = T[j][0]
                minj = j
        if flag is False:
            j = minj
        p = T[j][0]-T[i][0]
        i = j