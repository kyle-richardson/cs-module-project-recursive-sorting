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
    print(f'looking for {target} inside {arr}')
    sortedArr = merge_sort(arr)
    print(f'sorted: {sortedArr}')
    low = 0
    high = len(sortedArr) - 1
    mid = (low+high) // 2
    if target == sortedArr[mid]:
        return mid
    if len(sortedArr) == 1:
        return -1
    elif target < sortedArr[mid]:
        return agnostic_binary_search(sortedArr[:mid], target)
    else:
        nextArr = []
        if len(sortedArr) == 2:
            nextArr = sortedArr[1:]
        else:
            nextArr = sortedArr[mid:]
        right_side = agnostic_binary_search(nextArr, target)
        if right_side >= 0:
            print(mid + right_side)
            return mid + right_side
        else:
            return -1
