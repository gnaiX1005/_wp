def most_common(nums):
    count = {}
    for num in nums:
        count[num] = count.get(num, 0) + 1
    return max(count, key=count.get)

print(most_common([1, 3, 2, 3, 4, 3, 2]))  
