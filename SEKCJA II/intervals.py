def f(P):
    count = 0
    start = float('-inf')
    n = len(P)

    while True:

        mini = float('inf')
        for i in range(n):
            if P[i][0] >= start and P[i][1] < mini:
                mini = P[i][1]
        
        if mini == float('inf'):
            return count
            
        count += 1
        start = mini
    


P = [[1,2], [3,4], [4,5], [5,6]]
print(f(P))