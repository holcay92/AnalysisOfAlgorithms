# Python Code for Implementation and running time Algorithm
# Complexity plot of Heap Sort
# by Ashok Kajal
# This python code intends to implement Heap Sort Algorithm
# Plots its time Complexity on list of different sizes

# ---------------------Important Note -------------------
# numpy, time and matplotlib.pyplot are required to run this code
import time
from numpy.random import seed
from numpy.random import randint
import matplotlib.pyplot as plt


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
    B = list()
    heapSize1 = heapSize(A)
    for i in range(heapSize(A), 0, -1):
        A[0], A[i] = A[i], A[0]
        B.append(A[heapSize1])
        A = A[:-1]
        heapSize1 = heapSize1 - 1
        MaxHeapify(A, 0)


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



# randomly generates list of different
# sizes and call HeapSort function
elements = list()
times = list()
for i in range(1, 10):
    # generate some integers
    a = randint(0, 1000 * i, 1000 * i)
    # print(i)
    start = time.clock()
    HeapSort(a)
    end = time.clock()

    # print("Sorted list is ", a)
    print(len(a), "Elements Sorted by HeapSort in ", end - start)
    elements.append(len(a))
    times.append(end - start)

plt.xlabel('List Length')
plt.ylabel('Time Complexity')
plt.plot(elements, times, label='Heap Sort')
plt.grid()
plt.legend()
plt.show()
