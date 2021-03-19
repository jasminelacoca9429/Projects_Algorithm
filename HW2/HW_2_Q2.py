def quicksort(A, p, r):
    """A: array to be sorted
    p: left index
    q: right index"""
    if len(A) == 1:
        return A
    if p < r:
        """q is partitioning index, A[q] is not at right place"""
        q = partition(A, p, r)
        """Separately sort elements before and after partition"""
        quicksort(A, p, q)
        quicksort(A, q + 1, r)


def partition(A, p, r):
    """Function to partition for recursion"""
    pivot = A[p]

    i = p
    j = r

    while True:
        while A[i] <= pivot and i <= j:
            i += 1

        while A[j] >= pivot and i <= j:
            j -= 1

        if i < j:
            A[i], A[j] = A[j], A[i]

        else:
            break

    A[p], A[j] = A[j], A[p]
    return j

A = [13,19,9,5,12,8,7,4,11,2,6,21]

quicksort(A, 0, len(A) - 1)
print(A)
