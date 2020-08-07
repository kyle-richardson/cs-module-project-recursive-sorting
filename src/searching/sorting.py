
def merge_sort(arr):
    if len(arr) > 1:
        low = 0
        high = len(arr)
        mid = (low + high) // 2
        lhs = merge_sort(arr[:mid])
        rhs = merge_sort(arr[mid:])
        return merge(lhs, rhs)
    else:
        return arr


def merge(a, b):
    merged_arr = []
    a_curr_ind = 0
    b_curr_ind = 0
    while a_curr_ind < len(a) or b_curr_ind < len(b):
        if a_curr_ind >= len(a):
            merged_arr.append(b[b_curr_ind])
            b_curr_ind += 1
        elif b_curr_ind >= len(b):
            merged_arr.append(a[a_curr_ind])
            a_curr_ind += 1
        elif a[a_curr_ind] <= b[b_curr_ind]:
            merged_arr.append(a[a_curr_ind])
            a_curr_ind += 1
        else:
            merged_arr.append(b[b_curr_ind])
            b_curr_ind += 1
    return merged_arr

# STRETCH: implement the recursive logic for merge sort in a way that doesn't
# utilize any extra memory
# In other words, your implementation should not allocate any additional lists
# or data structures; it can only re-use the memory it was given as input


# def merge_in_place(arr, start, mid, end):


# def merge_sort_in_place(arr, l, r):
    # Your code here
