def merge(first1, first2):
    if first1 is None:
        return first2
    if first2 is None:
        return first1
    if first1.val > first2.val:
        first1, first2 = first2, first1
    First = first1
    first1 = first1.next
    p = First
    p.next = None
    val1 = first1
    val2 = first2
    while val1 is not None and val2 is not None:
        if val1.val > val2.val:
            first1, first2 = first2, first1
        p.next = first1
        first1 = first1.next
        p = p.next
        p.next = None
    if val1 is None:
        p.next = val2
    elif val2 is None:
        p.next = val1
    return First

def MergeSort(L): #L wskaznik do linked listy
    heads = []
    heads.append(L)
    if L.next is None:
        return L
    curr = L.next
    while curr is not None:
        if curr.val >= L.val:
            L = L.next
            curr = curr.next
        else:
            heads.append(curr.val)
            L.next = None
            L = curr
            curr = curr.next
# Tutaj kompletujemy tablice wskaznikow na poczatek serii naturalnych
    while len(heads) > 1:
        heads2 = []
        while len(heads) > 1:
            merged = merge(heads[0], heads[1])
            heads2.append(merged)
            heads = heads[2]
            heads2.extend(heads)
            heads = heads2
    return heads[0]