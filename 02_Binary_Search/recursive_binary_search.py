import array as myarray
arr = myarray.array('i',[3, 6, 8, 12, 14, 17, 25, 29, 31, 36, 42, 47, 53, 55, 62])

def rec_binary_search(low, high, key):
    if low == high:
        if arr[low] == key:
            return low
        else:
            return -1
    else:
        mid = low + (high - low) // 2
        if arr[mid] == key:
            return mid
        elif arr[mid] > key:
            return rec_binary_search(low, mid - 1, key)
        else:
            return rec_binary_search(mid + 1, high, key)
    return -1

print(rec_binary_search(arr[0], len(arr) - 1, 42))
