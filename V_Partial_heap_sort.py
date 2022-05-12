# Reference: https://www.geeksforgeeks.org/heap-sort-for-decreasing-order-using-min-heap/

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
