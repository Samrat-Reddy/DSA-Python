import array as myarray

nums= myarray.array('i', [-1,0,3,5,9,12])

def binary_search(nums, target):
    low = 0
    high = len(nums) - 1

    while low <= high:
        mid = low + (high - low) // 2

        if target == nums[mid]:
            return mid
        elif target < nums[mid]:
            high = mid - 1
        else:
            low = mid + 1
    return -1

print(binary_search(nums, 9))