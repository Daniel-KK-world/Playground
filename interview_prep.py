nums = [2, 7, 11, 15]
target = 9  

def two_sum(nums, target):
    set = {}
    for i, num in enumerate(nums):
        complement = target - num
        if complement in set:
            return complement, num
        set[num] = i
    
print(two_sum(nums, 9))