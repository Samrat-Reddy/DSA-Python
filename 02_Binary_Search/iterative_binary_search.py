import array as myarray
arr = myarray.array('i',[3, 6, 8, 12, 14, 17, 25, 29, 31, 36, 42, 47, 53, 55, 62])

def binary_search(arr, key):
    low = 0
    high = len(arr) - 1

    while low <= high:
        mid = low + (high - low) // 2

        if key == arr[mid]:
            return mid
        elif key < arr[mid]:
            high = mid - 1
        else:
            low = mid + 1
    return -1

print(binary_search(arr, 42))
