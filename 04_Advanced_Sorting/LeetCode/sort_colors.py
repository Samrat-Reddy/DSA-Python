import array as myarray
nums = myarray.array('i',[2, 0, 2, 1, 1, 0])

def sort_color():
    for i in range(len(nums)):
        for j in range(len(nums) - 1):
            if nums[j] > nums[j + 1]:
                nums[j], nums[j + 1] = nums[j + 1], nums[j]
    return nums

print(sort_color())