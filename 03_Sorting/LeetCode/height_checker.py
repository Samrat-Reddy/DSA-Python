import array as myarray
heights = myarray.array('i',[1,1,4,2,1,3])

def height_checker(heights):
    expected = sorted(heights)

    count = 0
    for i in range(len(heights)):
        if heights[i] != expected[i]:
            count += 1
    return count

print(height_checker(heights))