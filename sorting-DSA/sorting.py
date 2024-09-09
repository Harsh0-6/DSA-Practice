''' 1. Bubble Sort - compares adajacent elements and swaps them.
                   - The algorithm gets its name from the way smaller
                     or larger elements "bubble up" to the top of the list.
'''

'''Working:  (use 2 loops. one for covering every element in array 
                    and second loop for the comparision and swaps.
                    )compare, compare, continue, repeat.
    Pseudocode- procedure bubbleSort( list : array of items )
                for all elements of list
                    if list[i-1] > list[i] then
                        swap( list[i-1], list[i] )
                    end if
                end for
                return list
                end procedure'''

# Implementaion
# def bubbleSort(nums):
#     n = len(nums)    
#     for i in range(n):
#         for j in range(0, n - i - 1):
#             if nums[j] > nums[j + 1]:
#                 nums[j], nums[j + 1] = nums[j + 1], nums[j] #Swap using tuple unpacking
#     return nums

# nums = [15, 11, 16, 12, 14]
# print(bubbleSort(nums))

'''2. Merge Sort: Theory
            - Intro - Merge sort is a widely used sorting algorithm.
                    - Follows divide and conquer principle.
                    - This algorithm is particularly effective for sorting large datasets, 
                       and is known for its 'efficiency and stability'.

         - Principle - Divide and Conquer: The algorithm breaks down a problem into smaller
                       subproblems, solves each subproblem 'recursively', and combines their
                       solutions.
                    - Recursion: Merge sort is inherently recursive, meaning it calls 
                       itself with smaller subarrays until the base case (subarrays of one element) 
                       is reached.
                    - Stability: Merge sort is a stable sorting algorithm, meaning that it maintains
                       the relative order of equal elements from the original array in the sorted array.

         - Working - divide, conquer, combine.
                 * divide- The algorithm begins by dividing the unsorted list into 
                    two approximately equal halves. This process is repeated recursively 
                    until each subarray contains a single element (which is inherently sorted).

                 * conquer- Once the list is divided into subarrays of one element, 
                    the algorithm starts merging these subarrays back together. 
                    During this merging process, the elements are compared and sorted.

                 * combine- The sorted subarrays are combined to form a larger sorted array.
                   This process continues until the entire array is merged back into a 
                   single sorted array.
'''
# Implementation.
# def merge_sort(arr):
#     if len(arr) > 1:
#         mid = len(arr)//2
    
#         # splitting array in two halves.
#         left_half = arr[:mid]
#         right_half = arr[mid:]

#         # Recursively sort both halves.
#         merge_sort(left_half)
#         merge_sort(right_half)

#         # Initialize the pointers for left_half, right_half, main array.
#         i = j = k = 0

#         # Merge the sorted halves back into the original array
#         while i < len(left_half) and j < len(right_half):
#             if left_half[i] < right_half[j]:
#                 arr[k] = left_half[i]
#                 i += 1
#             else:
#                 arr[k] = right_half[j]
#                 j += 1
#             k += 1

#         # Checking if any element was left in the left_half
#         while i < len(left_half):
#             arr[k] = left_half[i]
#             i += 1
#             k += 1

#         # Checking if any element was left in the right_half
#         while j < len(right_half):
#             arr[k] = right_half[j]
#             j += 1
#             k += 1

#     return arr

# nums = [38, 27, 23, 3, 9, 82, 10]
# sorted_nums = merge_sort(nums)
# print("Sorted array:", sorted_nums)

''' Time and Space Complexity
        'Time Complexity':
            Best Case: O(n log n)
            Average Case: O(n log n)
            Worst Case: O(n log n)
        Space Complexity: O(n) 
         due to the temporary arrays used during the merging process.

    Use Cases of Merge Sort
    1. Sorting Large Datasets: Merge sort is efficient for handling large datasets,
       especially when the data cannot fit entirely into memory (external sorting).
    2. Linked Lists: It is particularly suitable for sorting linked lists since it
       does not require random access to elements.
    3. Stable Sorting: When the 'stability of the sorting algorithm is a priority',
       'merge sort' is preferred over algorithms like 'quicksort'.
    4. Parallel Processing: The divide-and-conquer approach allows merge sort to 
       be easily parallelized, making it suitable for multi-core processors.
    5. Inversion Counting: Merge sort can be adapted to count inversions in an array,
       which is useful in various applications.

    Summary: In summary, merge sort is a powerful and efficient sorting algorithm that
        employs the divide-and-conquer strategy to sort elements. Its stability, guaranteed
        performance, and suitability for large datasets make it a popular choice in many 
        applications.
'''
#------------------------------------------------------------------#
#------------------------------------------------------------------#

'''Quick Sort: Quick sort is a highly efficient sorting algorithm that utilizes the 
               divide-and-conquer principle. It was developed by British computer scientist 
               Tony Hoare in 1959 and is known for its speed and efficiency in sorting large datasets.
    
    Working -
            Choosing a Pivot: The algorithm begins by selecting an element from the array
            as the pivot.
            The choice of pivot can significantly affect the performance of the algorithm.
            Common strategies include selecting the first element, the last element,
            the middle element, or even a random element.
            Partitioning: The array is partitioned into two sub-arrays:
            One sub-array contains elements less than the pivot.
            The other sub-array contains elements greater than the pivot.
            During this process, the pivot is placed in its correct position in the sorted array.
            Recursion: The algorithm then recursively applies the same process to the
            two sub-arrays created by the partitioning step. This continues until 
            the base case is reached, where the sub-array has one or no elements,
            which are inherently sorted.

    Principles: 
        Divide and Conquer: Quick sort breaks down a problem into smaller subproblems,
          solves each subproblem recursively, and combines their solutions.
        In-Place Sorting: Quick sort can be implemented in such a way that it requires
          only a small, constant amount of additional storage space, making it memory efficient.
        Comparison Sort: Quick sort is a comparison-based sorting algorithm, meaning it
          sorts elements based on comparisons.

    Time Complexity:
        Best Case: O(n.logn) (when the pivot divides the array into two equal halves).
        Average Case: O(n.logn)
        Worst Case: O(n*2)(when the pivot is consistently the smallest or largest element.)

    Space Complexity:
        O(logn) for the recursive stack space in the average case,
        O(n) in the worst case if the recursion depth is maximal.   

    Use Case:
        Sorting Large Datasets: Quick sort is efficient for large datasets and is often faster
          than other algorithms like merge sort or bubble sort due to its low overhead.
        In-Place Sorting: It is suitable for situations where memory usage is a concern
          since it can sort the array without requiring additional storage for another array.
        General Purpose Sorting: Quick sort is commonly used in various applications,
          including database sorting, data processing, and in programming languages'
          standard libraries.
        Randomized Quick Sort: The randomized version of quick sort is particularly useful
          in applications where the input data is unpredictable, as it helps avoid the 
          worst-case scenarios.
        Parallel Processing: The divide-and-conquer nature of quick sort allows it to 
          be efficiently parallelized, making it suitable for multi-core processors.
    '''

# Implementing Quick Sort.
def quick_sort(arr):
    if len(arr) <= 1:  # Base case array with 0 or 1 element is already sorted.
        return arr
    
    # Choosing the pivot (here we choose the last element as the pivot)
    pivot = arr[-1]

    # Partitioning the array into two halves
    left = [x for x in arr[:-1] if x <= pivot] # Elements less than or equal to pivot
    right = [x for x in arr[:-1] if x > pivot]  # Elements greater than pivot

    # Recursively applying quick_sort to the left and right halves
    return quick_sort(left) + [pivot] + quick_sort(right)

nums = [34, 7, 23, 32, 5, 62, 32, 23, 7, 34, 5, 1, 0, 99, 100]
sorted_nums = quick_sort(nums)
print("Sorted array:", sorted_nums)