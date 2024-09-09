# Implementing searching algorithms.

# 1. Linear Search.
# nums, data = [13, 10 , 19, 9, 11, 5, 4, 1, 3], 4
# i = 0

# while i < len(nums):
#     if nums[i] == data:
#         print("data found at index: ", i)
#         break
#     i += 1
# else:
#     print("data not found")

# 2. Binary Search - needs sorted array.
nums, data = [1, 3, 5, 6], 2
left = 0
right = len(nums) - 1

while left <= right:  
    mid = left + (right - left) // 2     
    if nums[mid] == data:
        print("Value found at index:", mid)
        break
    elif nums[mid] < data:
        left = mid + 1
    else:  # This covers the case where nums[mid] > data
        right = mid - 1  # Corrected line

# If the loop ends without finding the value
if left > right:
    print("Value not found")


    