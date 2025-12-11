class Solution:
    def summaryRanges(self, nums):
        if not nums:
            return nums

        ans=[]
        s=nums[0]
        cur=nums[0]
        for i in range(1,len(nums)):
            if nums[i] == cur+1:
                cur+=1
            else:
                if s==cur:
                    ans.append(f"{s}")
                else:
                    ans.append(f"{s}->{cur}")
                s=nums[i]
                cur=nums[i]
        if s==cur:
            ans.append(f"{s}")
        else:
            ans.append(f"{s}->{cur}")
            
        return ans

# 228. Summary Ranges

# Example 1:

# Input: nums = [0,1,2,4,5,7]
# Output: ["0->2","4->5","7"]
# Explanation: The ranges are:
# [0,2] --> "0->2"
# [4,5] --> "4->5"
# [7,7] --> "7"
