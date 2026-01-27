#Given an array of integers, return the count of numbers that contain an even number of digits. For example, 12, 7896, and 1771 are all even-numbered integers.  

nums = [2, 3, 45, 6789, 1234, 56, 7, 89012]


def count_even_digit_numbers(nums):
    even_count = 0
    for num in nums:
        if len(str(num)) % 2 == 0:
            even_count += 1
    return even_count 
print(count_even_digit_numbers(nums))


