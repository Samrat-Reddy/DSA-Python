import array as myarray

nums = myarray.array('i', [1,3,5,6])

def search_insert_position(nums, target):
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
    return low

print(search_insert_position(nums, 5))