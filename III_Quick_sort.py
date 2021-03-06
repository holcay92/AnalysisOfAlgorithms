def pivot(array, start, end):
    # Reference: https://www.askpython.com/python/examples/quicksort-algorithm
    # Sort all elements by Quick-sort and return the πβth element in the list.
    # While partitioning choose the pivot element as the first element in an array.

    pivot = array[start]
    low = start + 1
    high = end

    while True:
        while low <= high and array[high] >= pivot:
            high = high - 1
        while low <= high and array[low] <= pivot:
            low = low + 1
        if low <= high:
            array[low], array[high] = array[high], array[low]
        else:
            break
    array[start], array[high] = array[high], array[start]
    return high


def quick_sort(array, start, end):
    if start >= end:
        return
    p = pivot(array, start, end)
    quick_sort(array, start, p - 1)
    quick_sort(array, p + 1, end)

