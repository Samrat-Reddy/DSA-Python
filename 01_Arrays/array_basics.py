import array as myarray

#Initialisation
arr = myarray.array('i',[])

#Insertion
arr.insert(0,1)
arr.insert(1,2)
arr.insert(2,3)
arr.insert(3,4)
print(arr)

arr.append(5)
print(arr)

#Traversal
for elements in arr:
    print(elements)

#Deletion
arr.pop(2)
print(arr)

#Update
arr[3] = 40
print(arr)

#Linear Search
for i in range(len(arr)):
    if arr[i] == 5:
        print("Element found at index", i)
        break
    else:
        print("Element not found")
        break