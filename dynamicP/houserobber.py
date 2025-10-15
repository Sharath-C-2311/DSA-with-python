
# You are given an array nums representing the amount of money in each house.
#  You cannot rob two adjacent houses. Return the maximum amount of money you can rob.

class Solution:
    def rob(self, nums):
        if not nums:
            return None
        if len(nums)==1:
            return nums[0]
        dp=[0]*len(nums)
        dp[0] = nums[0]
        dp[1] = max(nums[0],nums[1])

        for i in range(2,len(nums)):
            dp[i] = max(dp[i-1],dp[i-2]+nums[i])
        return dp[-1]