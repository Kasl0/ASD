"""
Zad. 3
A - tablica liczb naturalnych
Znaleść najdłuższy podciąg A w którym wyrazy są rosnące.
Złożoność O(nlogn)
"""

def bin_search(a, T):
    n = len(T)
    if n == 0: return -1
    l = 0
    p = n - 1
    mid = (l + p) // 2

    while l <= p: 
        mid = (l + p) // 2
        if T[mid][-1] >= a and (mid == 0 or T[mid - 1][-1] < a):
            return mid
        elif T[mid][-1] > a:
            p = mid - 1
        else:
            l = mid + 1
    return -1

def f(A):
    n = len(A)
    T = []
    for a in A:
        index = bin_search(a, T)
        if index == -1:
            T.append([a])
        else: 
            T[index].append(a)
    print(T)
    return len(T)

A = [7, 3, 15, 1, 4, 5, 16, 1, 8]
print(f(A))

def lower_bound(f, l, r, v):
	while l < r:
		mid = (l + r) // 2
		if f[mid] < v:
			l = mid + 1
		else:
			r = mid
	return l

def lis(A):
	f = [-1 for i in range(len(A)+1)]
	f[0] = 0
	maxlen = 0
	for i in A:
		pos = lower_bound(f, 0, maxlen + 1, i)
		
		if f[pos+1] < 0 or f[pos+1] > i:
			f[pos+1] = i
		print(f[:maxlen+1])
		maxlen = max(maxlen, pos+1)
	return maxlen

A = [7, 3, 15, 1, 4, 5, 16, 1, 8]
print(lis(A))
