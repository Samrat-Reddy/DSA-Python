import array as myarray
arr = myarray.array('i',[8, 3, 5, 4, 7, 6, 1, 2])

def merge_sort(low, high):
    if low < high:
        mid = low + (high - low) // 2
        merge_sort(low, mid)
        merge_sort(mid + 1, high)
        merge(low, mid, high)
    return arr

def merge(low, mid, high):
    left_sub = arr[low: mid + 1]
    right_sub = arr[mid + 1: high + 1]

    i = 0
    j = 0
    k = low

    while i < len(left_sub) and j < len(right_sub):
        if left_sub[i] <= right_sub[j]:
            arr[k] =  left_sub[i]
            i += 1
        else:
            arr[k] = right_sub[j]
            j += 1
        k += 1

    while i < len(left_sub):
        arr[k] = left_sub[i]
        i += 1
        k += 1

    while j < len(right_sub):
        arr[k] = right_sub[j]
        j += 1
        k += 1

print(merge_sort(0, len(arr) - 1))