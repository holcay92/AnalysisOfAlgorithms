# Sorting with insertion sort
def insertionSort(arr):
    # Reference : https://www.geeksforgeeks.org/python-program-for-insertion-sort/
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

# Driver code
array = [5,1,8,2,7,6,3,4]
print("please enter the k value: ")
k = int(input())
insertionSort(array)
print(array[k - 1])