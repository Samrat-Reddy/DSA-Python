import array as myarray
nums = myarray.array('i',[3,1,2,4])

def sor_parity(nums):
    pos = 0

    for i in range(len(nums)):
        if nums[i] % 2 == 0:
            nums[i], nums[pos] = nums[pos], nums[i]
            pos += 1
    return nums

print(sor_parity(nums))
