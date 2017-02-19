def partition(A, lo, hi):
    pivot = A[hi]
    i = lo

    for j in range(lo, hi):
        if A[j] <= pivot:
            A[i], A[j] = A[j], A[i]
            i += 1

    A[i], A[hi] = A[hi], A[i]
    return i

def nsmallest(m, A):
    i = 0
    q = partition(A, 0, len(A)-1)
    if i < q:
        partition(A, 0, q-1)
        i+=1
    else:
        partition(A, q+1, len(A)-1)
        i+=1
    
    return A[:m:]

    
    """
    Возвращает `m` наименьших элементов массива A.
    Функция реализована на основе Quicksort.
    >>> nsmallest(3, [44, 64, 21, 86, 40, 46, 95])
    [21, 40, 44]
    """
print(nsmallest(4,[44, 64, 21, 86, 40, 46, 95]))

