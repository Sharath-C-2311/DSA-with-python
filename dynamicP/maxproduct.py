#program to find subarray with max product

class Solution:
    def maxProduct(self, nums):
        p=1
        s=1
        res=float('-inf')
        n=len(nums)
        for i in range(n):
            if p==0:
                p=1
            if s==0:
                s=1
            p*=nums[i]
            s*=nums[n-1-i]
            res = max(res,max(p,s))

        return res


# Dynamic programming method 
# class Solution:
#     def maxProduct(self, nums):
#         result = nums[0]
#         cur_max = nums[0]
#         cur_min = nums[0]

#         for i in range(1,len(nums)):
#             temp = max(nums[i],cur_max*nums[i],cur_min*nums[i])
#             cur_min = min(nums[i],cur_max*nums[i],cur_min*nums[i])
#             cur_max = temp
#             result = max(result,cur_max)
#         return result