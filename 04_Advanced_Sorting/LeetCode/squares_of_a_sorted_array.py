import array as myarray
nums = myarray.array('i',[-4, -1, 0, 3, 10])

def squares_sort():
    n = len(nums)
    res = [0] * n
    left, right = 0, n - 1

    for i in range(n - 1, -1, -1):
        if abs(nums[left]) > abs(nums[right]):
            res[i] = nums[left] * nums[left]
            left += 1
        else:
            res[i] = nums[right] * nums[right]
            right -= 1
    return res

print(squares_sort())