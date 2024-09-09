'''Two Pointers Technique
     The two pointers technique is a popular algorithmic strategy used to solve
     various problems, especially those involving arrays or linked lists. It involves
     using two pointers that traverse the data structure at different speeds or from
     different starting points to achieve a specific goal. This technique is 
     particularly effective for problems related to "searching", "sorting", and "merging".
     
     Applications
        The two pointers technique can be applied to a variety of problems, 
            including:
            "Finding pairs": Identifying pairs in a sorted array that sum to a specific value.
            "Reversing a string": Using two pointers to swap characters from the beginning
              and end of a string.
            "Merging sorted arrays": Efficiently merging two sorted arrays into one.
            "Partitioning": Rearranging elements based on certain criteria, such as
              separating even and odd numbers.
     '''

# 1. Finding pairs(Sorted Array).
def has_pair_with_sum(nums, target):
    left, right = 0, len(nums) - 1
    while left < right:
        pair_sum = nums[left] + nums[right]
        if pair_sum < target:
            left += 1
        elif pair_sum > target:
            right -= 1
        else:
            return True

    return False

# nums = [1, 2, 3, 4, 6]
# target = 10
# print(has_pair_with_sum(nums, target))

# 2. Reverse a string - 
# 2.1 -(converting string to a list.)
# def rev_str(s: str) ->str:
#    s_list = list(s) # Convert the string to a list to allow mutability.
#    left = 0
#    right = len(s_list) - 1
#    while left < right:
#         s_list[left], s_list[right] = s_list[right], s_list[left]'''Swap using tuple unpacking'''
#         left += 1
#         right -= 1

#    # Convert the list back to a string
#    return ''.join(s_list)

# str_to_rev = 'harshxrajawat'
# new_str = rev_str(str_to_rev)
# print(new_str, end=" ")

# 2.1 - Reversing a string - Using slicing.
# def rev_str(s: str) -> str:
#     return s[::-1]

# str_to_reverse = 'harsh'
# new_str = rev_str(str_to_reverse)
# print(new_str)

# 2.2 - Using the reversed() Function.
'''You can also use the built-in reversed() function, which returns an iterator
that accesses the given sequence in the reverse order.'''
# def rev_str(s: str) -> str:
#     return ''.join(reversed(s))

# str_to_reverse = 'rajawatx'
# new_str = rev_str(str_to_reverse)
# print(new_str)

# 2.3 - Using a Loop
'''If you want to reverse a string manually without converting it to a list, you
   can use a loop to build the reversed string. This method is "less efficient" but
   demonstrates the concept clearly.'''

# def rev_str(s: str) -> str:
#     reversed_str = ''
#     for char in s:
#         reversed_str = char + reversed_str  # Prepend the character
#     return reversed_str

# str_to_reverse = 'harshxrajawat'
# new_str = rev_str(str_to_reverse)
# print(new_str)