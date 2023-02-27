def insertion_sort(array):
    n = len(array)
    for i in range(1, n):
        j = i
        while(j-1>0 and array[j]<array[j-1]):
            array[j-1], array[j] = array[j], array[j-1]
            j -= 1
    return array

def bubble_sort(array):
    n = len(array)
    for i in range(n-1):
        for j in range(1,n):
            if array[j-1] > array[j]: array[j-1], array[j] = array[j], array[j-1]
    return array

def selection_sort(array):
    n = len(array)
    for i in range(n):
        mini = array[i]
        mini_index = i
        for j in range(i+1, n):
            if array[j] < mini:
                mini = array[j]
                mini_index = j
        array[i], array[mini_index] = array[mini_index], array[i]
    return array

t = [3,24,4,12]
print(insertion_sort(t))
print(bubble_sort(t))
print(selection_sort(t))