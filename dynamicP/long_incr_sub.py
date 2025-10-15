# dp approach

class Solution:
    def lengthOfLIS(self, nums):
        res=[1]*len(nums)
        m = nums[0]
        mx = nums[0]
        for i in range(1,len(nums)):
            for j in range(0,i):
                if nums[j] < nums[i]:
                    res[i] = max(res[i],res[j]+1)
        return max(res)
    
#simple approach

# class Solution:
#     def lengthOfLIS(self, nums: List[int]) -> int:
#         res=[]
#         for i in nums:
#             if not res or res[-1] < i:
#                 res.append(i)
#             else:
#                 p = bisect_left(res,i)
#                 res[p] = i
            
#         return len(res)


# Given an integer array nums, return the length of the longest strictly increasing subsequence.

# Example 1:

# Input: nums = [10,9,2,5,3,7,101,18]
# Output: 4
# Explanation: The longest increasing subsequence is [2,3,7,101], therefore the length is 4.