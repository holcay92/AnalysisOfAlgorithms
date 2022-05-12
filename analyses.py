import random
import time
from timeit import default_timer as timer
from numpy.random import seed
from numpy.random import randint
import matplotlib.pyplot as plt
import sys
sys.setrecursionlimit(9000)



# find left child of node i
def left(i):
    return 2 * i + 1


# find right child of node i
def right(i):
    return 2 * i + 2


# calculate and return array size
def heapSize(A):
    return len(A) - 1


# This function takes an array and Heapyfies
# the at node i
def MaxHeapify(A, i):
    # print("in heapy", i)
    l = left(i)
    r = right(i)

    # heapSize = len(A)
    # print("left", l, "Rightt", r, "Size", heapSize)
    if l <= heapSize(A) and A[l] > A[i]:
        largest = l
    else:
        largest = i
    if r <= heapSize(A) and A[r] > A[largest]:
        largest = r
    if largest != i:
        # print("Largest", largest)
        A[i], A[largest] = A[largest], A[i]
        # print("List", A)
        MaxHeapify(A, largest)


# this function makes a heapified array
def BuildMaxHeap(A):
    for i in range(int(heapSize(A) / 2) - 1, -1, -1):
        MaxHeapify(A, i)


# Sorting is done using heap of array
def HeapSort(A):
    BuildMaxHeap(A)
    B = []
    heapSize1 = heapSize(A)
    for i in range(heapSize(A), 0, -1):
        A[0], A[i] = A[i], A[0]
        B.append(A[heapSize1])
        A = A[:-1]
        heapSize1 = heapSize1 - 1
        MaxHeapify(A, 0)
    B.reverse()
    return B


# Sorting with insertion sort
def insertionSort(arr):
    # Traverse through 1 to len(arr)
    for i in range(1, len(arr)):

        key = arr[i]

        # Move elements of arr[0..i-1], that are
        # greater than key, to one position ahead
        # of their current position
        j = i - 1
        while j >= 0 and key < arr[j]:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key
    return arr


def heapify(arr, n, i):
    largest = i  # Initialize largest as root
    l = 2 * i + 1  # left = 2*i + 1
    r = 2 * i + 2  # right = 2*i + 2

    # See if left child of root exists and is
    # greater than root
    if l < n and arr[i] < arr[l]:
        largest = l

    # See if right child of root exists and is
    # greater than root
    if r < n and arr[largest] < arr[r]:
        largest = r

    # Change root, if needed
    if largest != i:
        arr[i], arr[largest] = arr[largest], arr[i]  # swap

        # Heapify the root.
        heapify(arr, n, largest)

def partialHeapSort(A, k):
    n = len(A)
    for i in range(n//2 - 1, -1, -1):
        heapify(A, n, i)
    for i in range(n - k, 0, -1):
        A[i], A[0] = A[0], A[i]
        heapify(A, i, 0)
    return A


def pivot(array, start, end):
    # Reference: https://www.askpython.com/python/examples/quicksort-algorithm
    # Sort all elements by Quick-sort and return the 𝑘’th element in the list.
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




def merge(arr, l, m, r):
    # Reference: https://www.geeksforgeeks.org/python-program-for-merge-sort/

    n1 = m - l + 1
    n2 = r - m

    # create temp arrays
    L = [0] * (n1)
    R = [0] * (n2)

    # Copy data to temp arrays L[] and R[]
    for i in range(0, n1):
        L[i] = arr[l + i]

    for j in range(0, n2):
        R[j] = arr[m + 1 + j]

    # Merge the temp arrays back into arr[l..r]
    i = 0  # Initial index of first subarray
    j = 0  # Initial index of second subarray
    k = l  # Initial index of merged subarray

    while i < n1 and j < n2:
        if L[i] <= R[j]:
            arr[k] = L[i]
            i += 1
        else:
            arr[k] = R[j]
            j += 1
        k += 1

    # Copy the remaining elements of L[], if there
    # are any
    while i < n1:
        arr[k] = L[i]
        i += 1
        k += 1

    # Copy the remaining elements of R[], if there
    # are any
    while j < n2:
        arr[k] = R[j]
        j += 1
        k += 1


# l is for left index and r is right index of the
# sub-array of arr to be sorted

def mergeSort(arr, l, r):
    if l < r:
        # Same as (l+r)//2, but avoids overflow for
        # large l and h
        m = l + (r - l) // 2

        # Sort first and second halves
        mergeSort(arr, l, m)
        mergeSort(arr, m + 1, r)
        merge(arr, l, m, r)
        return arr

def swap(nums, i, j):
    temp = nums[i]
    nums[i] = nums[j]
    nums[j] = temp


def partition(nums, left, right, pIndex):
    # Pick leftmost element as a pivot from the list
    pivot = nums[left]

    # Move pivot to end
    swap(nums, pIndex, right)

    # elements less than the pivot will be pushed to the left of `pIndex`;
    # elements more than the pivot will be pushed to the right of `pIndex`;
    # equal elements can go either way
    pIndex = left

    # each time we find an element less than or equal to the pivot, `pIndex`
    # is incremented, and that element would be placed before the pivot.
    for i in range(left, right):
        if nums[i] <= pivot:
            swap(nums, i, pIndex)
            pIndex = pIndex + 1

    # Move pivot to its place
    swap(nums, pIndex, right)

    # return `pIndex` (index of the pivot element)
    return pIndex


# Returns the k'th smallest element in a list within `left…right`
# (i.e., left <= k <= right). The search space within the list is
# changing for each round – but the list is still the same size.
# Thus, `k` does not need to be updated with each round.
def quickSelect(nums, left, right, k):
    # If the list contains only one element, return that element
    if left == right:
        return nums[left]

    # select `pIndex` between left and right
    pIndex = left

    pIndex = partition(nums, left, right, pIndex)

    # The pivot is in its sorted position
    if k == pIndex:
        return nums[k]

    # if `k` is less than the pivot index
    elif k < pIndex:
        return quickSelect(nums, left, pIndex - 1, k)

    # if `k` is more than the pivot index
    else:
        return quickSelect(nums, pIndex + 1, right, k)

def bigger(a, b):
    if a > b:
        return a
    else:
        return b


def median(a, b, c):
    x = bigger(a, bigger(b, c))
    if x == a:
        return bigger(b, c)
    if x == b:
        return bigger(a, c)
    else:
        return bigger(a, b)


def swap(nums, i, j):
    temp = nums[i]
    nums[i] = nums[j]
    nums[j] = temp


def partition(nums, left, right, pIndex):
    # Pick leftmost element as a pivot from the list
    mid = int((left+right)/2)
    pivot = median(nums[left], nums[mid], nums[right])
    # print(pivot)
   # print(pIndex)

    # Move pivot to end
    swap(nums, pIndex, right)

    # elements less than the pivot will be pushed to the left of `pIndex`;
    # elements more than the pivot will be pushed to the right of `pIndex`;
    # equal elements can go either way
    pIndex = left

    # each time we find an element less than or equal to the pivot, `pIndex`
    # is incremented, and that element would be placed before the pivot.
    for i in range(left, right):
        if nums[i] <= pivot:
            swap(nums, i, pIndex)
            pIndex = pIndex + 1

    # Move pivot to its place
    swap(nums, pIndex, right)

    # return `pIndex` (index of the pivot element)
    return pIndex


# Returns the k'th smallest element in a list within `left…right`
# (i.e., left <= k <= right). The search space within the list is
# changing for each round – but the list is still the same size.
# Thus, `k` does not need to be updated with each round.
def quickSelectMedian(nums, left, right, k):
    # If the list contains only one element, return that element
    if left == right:
        return nums[left]

    # select `pIndex` between left and right
    mid = int((left + right) / 2)
    pivot = median(nums[left], nums[mid], nums[right])
    pIndex = nums.index(pivot)

    pIndex = partition(nums, left, right, pIndex)

    # The pivot is in its sorted position
    if k == pIndex:
        return nums[k]

    # if `k` is less than the pivot index
    elif k < pIndex:
        return quickSelect(nums, left, pIndex - 1, k)

    # if `k` is more than the pivot index
    else:
        return quickSelect(nums, pIndex + 1, right, k)

def partialSelectionSort(array, k):
    # Reference: https://www.geeksforgeeks.org/selection-algorithms/

    for i in range(0, k):
        minIndex = i
        minValue = array[i]

        for j in range(i + 1, len(array)):
            if array[j] < minValue:
                minIndex = j
                minValue = array[j]

                array[i], array[minIndex] = array[minIndex], array[i]

def readInputFile(inputFile):
    inputs = []
    with open(inputFile, "r") as fl:
        number = ""
        for x in fl.readline():
            if x == " ":
                inputs.append(int(number))
                number = ""
                continue
            number += x
    return inputs

result=[]

a=[]
b=0
x = readInputFile("quickSortWorstInput" + "5" + ".txt")
start = timer()
quick_sort(x,0,len(x)-1)
duration3 = timer() - start
a.append(len(x))
b=(duration3)
result.append(b)
print(b)
plt.title("Insertion sort")
plt.xlabel("Input Size(n)")
plt.ylabel("Time(s)")
plt.plot(a, b, 'r')

a=[]
b=0
x = readInputFile("quickSortWorstInput" + "5" + ".txt")
start = timer()
quick_sort(x,0,len(x)-1)
duration3 = timer() - start
a.append(len(x))
b=(duration3)
result.append(b)
print(b)
plt.title("Insertion sort")
plt.xlabel("Input Size(n)")
plt.ylabel("Time(s)")
plt.plot(a, b, 'r')

a=[]
b=0
x = readInputFile("quickSortWorstInput" + "5" + ".txt")
start = timer()
quick_sort(x,0,len(x)-1)
duration3 = timer() - start
a.append(len(x))
b=(duration3)
result.append(b)
print(b)
plt.title("Insertion sort")
plt.xlabel("Input Size(n)")
plt.ylabel("Time(s)")
plt.plot(a, b, 'r')

a=[]
b=0
x = readInputFile("quickSortWorstInput" + "5" + ".txt")
start = timer()
quick_sort(x,0,len(x)-1)
duration3 = timer() - start
a.append(len(x))
b=(duration3)
result.append(b)
print(b)
plt.title("Insertion sort")
plt.xlabel("Input Size(n)")
plt.ylabel("Time(s)")
plt.plot(a, b, 'r')

a=[]
b=0
x = readInputFile("quickSortWorstInput" + "5" + ".txt")
start = timer()
quick_sort(x,0,len(x)-1)
duration3 = timer() - start
a.append(len(x))
b=(duration3)
result.append(b)
print(b)
plt.title("Insertion sort")
plt.xlabel("Input Size(n)")
plt.ylabel("Time(s)")
plt.plot(a, b, 'r')

a=[]
b=0
x = readInputFile("quickSortWorstInput" + "5" + ".txt")
start = timer()
quick_sort(x,0,len(x)-1)
duration3 = timer() - start
a.append(len(x))
b=(duration3)
result.append(b)
print(b)
plt.title("Insertion sort")
plt.xlabel("Input Size(n)")
plt.ylabel("Time(s)")
plt.plot(a, b, 'r')

a=[]
b=0
x = readInputFile("quickSortWorstInput" + "5" + ".txt")
start = timer()
quick_sort(x,0,len(x)-1)
duration3 = timer() - start
a.append(len(x))
b=(duration3)
result.append(b)
print(b)
plt.title("Insertion sort")
plt.xlabel("Input Size(n)")
plt.ylabel("Time(s)")
plt.plot(a, b, 'r')

a=[]
b=0
x = readInputFile("quickSortWorstInput" + "5" + ".txt")
start = timer()
quick_sort(x,0,len(x)-1)
duration3 = timer() - start
a.append(len(x))
b=(duration3)
result.append(b)
print(b)
plt.title("Insertion sort")
plt.xlabel("Input Size(n)")
plt.ylabel("Time(s)")
plt.plot(a, b, 'r')

a=[]
b=0
x = readInputFile("quickSortWorstInput" + "5" + ".txt")
start = timer()
quick_sort(x,0,len(x)-1)
duration3 = timer() - start
a.append(len(x))
b=(duration3)
result.append(b)
print(b)
plt.title("Insertion sort")
plt.xlabel("Input Size(n)")
plt.ylabel("Time(s)")
plt.plot(a, b, 'r')

a=[]
b=0
x = readInputFile("quickSortWorstInput" + "5" + ".txt")
start = timer()
quick_sort(x,0,len(x)-1)
duration3 = timer() - start
a.append(len(x))
b=(duration3)
result.append(b)
print(b)
plt.title("Insertion sort")
plt.xlabel("Input Size(n)")
plt.ylabel("Time(s)")
plt.plot(a, b, 'r')

print(sum(result) / len(result))
