class Solution:
    def minSubArrayLen(self, target, nums):
        pre=0
        req=float("inf")
        i=0
        j=0
        
        for j in range(len(nums)):
                pre+=nums[j]
                while pre>=target:
                    if j-i+1<req:
                        req=j-i+1
                    pre-=nums[i]
                    i+=1
        
        if req==float("inf"):
            return 0
        return req
    
# 209. Minimum Size Subarray Sum

# Example 1:

# Input: target = 7, nums = [2,3,1,2,4,3]
# Output: 2
# Explanation: The subarray [4,3] has the minimal length under the problem constraint.
