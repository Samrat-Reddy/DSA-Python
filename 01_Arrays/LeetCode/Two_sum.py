import array as myarray

nums = myarray.array('i',[2,7,11,15])
for i in range(len(nums)):
    for j in range(i + 1, len(nums)):
        if nums[i] + nums[j] == 9:
            print(nums[i], nums[j])