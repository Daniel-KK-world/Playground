def find_missing_number(nums):
    n = len(nums)
    nums_set = set(nums)  
    for num in range(n+1):
        if num not in nums_set:
            return num
        
    return None


nums = [0, 1]
print(find_missing_number(nums))