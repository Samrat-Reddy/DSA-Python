import array as myarray
arr = myarray.array('i',[5, 1, 9, 2, 6, 3])

def insertion_sort(arr):
    for i in range(len(arr)):
        temp = arr[i]
        j = i - 1

        while j >= 0 and arr[j] > temp:
            arr[j + 1] = arr[j]
            j = j - 1

        arr[j + 1] = temp
    return arr

print(insertion_sort(arr))