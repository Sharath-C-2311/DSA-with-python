# Given an integer array nums, return an array answer such that 
# answer[i] is equal to the product of all the elements of nums except nums[i].

class Solution:
    def productExceptSelf(self, nums):
        flag=0
        ans=[]
        for i in nums:
            if i==0:
                flag+=1
        prod=1
        if flag==1:
            for i in nums:
                if i!=0:
                    prod*=i
            ans=[0]*len(nums)
            for i in range(len(nums)):
                if nums[i]==0:
                    ans[i]=prod
        elif flag>1:
            ans=[0]*len(nums)
        else:
            for i in nums:
                prod*=i
            for i in nums:
                ans.append(prod//i)
        return ans