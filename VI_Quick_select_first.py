# Reference: https://www.geeksforgeeks.org/quickselect-algorithm/
#           https://www.techiedelight.com/quickselect-algorithm/

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

