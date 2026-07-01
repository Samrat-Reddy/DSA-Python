import array as myarray
arr = myarray.array('i',[8, 3, 5, 4, 7, 6, 1, 2])

def partition(arr, low, high):
    pivot = arr[low]
    i = low
    j = high

    while i < j:
        while True:
            if arr[i] > pivot:
                break

        while True:
            if arr[j] <= pivot:
                break

        if i < j:
            arr[i], arr[j] = arr[j], arr[i]
        arr[low], arr[j] = arr[j], arr[low]
    return j

def quick_sort(arr, low, high):
    if low < high:
        j = partition(arr, low, high)
        quick_sort(arr,low, j)
        quick_sort(arr, j+1, high)
    return arr

print(quick_sort(arr, 0, len(arr)-1))