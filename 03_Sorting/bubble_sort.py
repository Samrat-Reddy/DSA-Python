import array as myarray
arr = myarray.array('i',[5, 1, 9, 2, 6, 3])

def bubble_sort(arr):
    flag = 0
    for i in range(len(arr)-1):
        for j in range(len(arr)-1-i):
            if arr[j] > arr[j + 1]:
                temp = arr[j]
                arr[j] = arr[j + 1]
                arr[j + 1] = temp
                flag = 1
        if flag == 0:
            break
    return arr

print(bubble_sort(arr))