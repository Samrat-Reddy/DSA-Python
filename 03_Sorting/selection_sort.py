import array as myarray
arr = myarray.array('i',[5, 1, 9, 2, 6, 3])

def selection_sort(arr):
    for i in range(len(arr) - 1):
        min = i
        for j in range(i + 1, len(arr)):
            if arr[j] < arr[min]:
                min = j
        if min != i:
            temp = arr[i]
            arr[i] = arr[min]
            arr[min] = temp
    return arr

print(selection_sort(arr))
