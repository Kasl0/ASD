def zad(M):
    size = len(M)
    color = [0] * size
    color[0] = 1
    dfs(M, color, 0)

def dfs(M, color, n):
    curr_call = color[n]
    size = len(M)
    for i in range(size):
        if M[n][i] == 1:
            if color[i] == curr_call:
                return False
            if color[i] == 0:
                if curr_call == 1:
                    color[i] = 2
                else:
                    color[i] = 1
        if not dfs(M, color, i):
            return False
    return False

