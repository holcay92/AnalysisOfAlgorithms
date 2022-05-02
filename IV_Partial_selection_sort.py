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

    print(array[k - 1])


# Driver code
array = [5, 1, 8, 2, 7, 6, 3, 4]
print("please enter the k value: ")
k = int(input())
partialSelectionSort(array, k)
