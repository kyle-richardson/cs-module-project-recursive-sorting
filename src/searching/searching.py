from sorting import merge_sort

# TO-DO: Implement a recursive implementation of binary search


def binary_search(arr, target, low, high):
    # Your code here
    sortedArr = merge_sort(arr)
    if low > high:
        return -1
    else:
        mid = (low+high) // 2
        if target == sortedArr[mid]:
            return mid
        elif target < sortedArr[mid]:
            return binary_search(sortedArr, target, low, mid-1)
        else:
            return binary_search(sortedArr, target, mid+1, high)


# STRETCH: implement an order-agnostic binary search
# This version of binary search should correctly find
# the target regardless of whether the input array is
# sorted in ascending order or in descending order
# You can implement this function either recursively
# or iteratively
def agnostic_binary_search(arr, target):
    first = 0
    last = len(arr) - 1
    is_ascending = True
    if arr[1] < arr[0]:
        is_ascending = False
    while first <= last:
        mid = (first+last) // 2
        if target == arr[mid]:
            return mid
        elif target < arr[mid]:
            if is_ascending:
                last = mid - 1
            else:
                first = mid + 1
        else:
            if is_ascending:
                first = mid + 1
            else:
                last = mid - 1
    return -1
