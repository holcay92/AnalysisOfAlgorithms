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

