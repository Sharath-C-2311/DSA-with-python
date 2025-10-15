class Solution:
    def longestConsecutive(self, nums):
        if len(nums)==0:
            return 0
        nums.sort()
        count=1
        max_count=1

        for i in range(len(nums)-1):
            if nums[i] == (nums[i+1]-1):
                count+=1
            else:
                if nums[i]!=nums[i+1]:
                    max_count = max(max_count,count)
                    count=1
        max_count = max(max_count,count)
        return max_count
    
# Given an unsorted array of integers nums, 
# return the length of the longest consecutive elements sequence.

# Example 1:

# Input: nums = [100,4,200,1,3,2]
# Output: 4
# Explanation: The longest consecutive elements sequence is [1, 2, 3, 4]. Therefore its length is 4.
# Example 2:

# Input: nums = [0,3,7,2,5,8,4,6,0,1]
# Output: 9
# Example 3:

# Input: nums = [1,0,1,2]
# Output: 3

# more efficiet takes only o(n) time
# class Solution:
#     def longestConsecutive(self, nums):
#         # Convert nums into a set for O(1) lookups
#         s = set(nums)
#         ans = 0

#         # Iterate through each number in the set
#         for i in s:
#             # Only start counting if 'i' is the beginning of a sequence
#             # i.e., there's no (i-1) in the set

#             if i - 1 not in s: #this takes only o(1) time

#                 l = 1  # length of current sequence
#                 # Keep checking next consecutive numbers
#                 while i + l in s:
#                     l += 1
#                 # Update longest sequence found so far
#                 ans = max(ans, l)

#         return ans

