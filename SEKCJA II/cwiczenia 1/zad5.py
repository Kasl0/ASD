"""
Zad. 5
A - liczby naturalne - nominały
T - kwota, którą chcemy wydać
Ile minimalnie monet należy wydać aby wydać kwotę T?
"""

# f(i) = min f(i-a) + 1

"""
def wydawanie(A, T, B):
	for a in A:
		if a == T:
			return 1
	if B[T]>0:
		return B[T]
	min = wydawanie(A,T-A[0],B) + 1
	for i in range(1,len(A)):
		tmp = wydawanie(A,T-A[i],B) + 1
		if tmp < min:
			min = tmp
	B[T] = min
	return B[T]
"""

def coins(N, T):
	B = [0 for i in range(T+1)]
	for i in range(1, T+1):
		min = -1
		for n in N:
			if i - n >= 0:
				if min < 0 or B[i-n] + 1 < min:
					min = B[i-n] + 1
		B[i] = min
	return B[T]

N = [1,5,8]
T = 15	
print(coins(N, T))