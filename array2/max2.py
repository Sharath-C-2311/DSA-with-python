#find the numbers that appears more than n/3 times , where n is the size of array
#i have used voting algo to find it time -> n , space -> constant
class Solution:
    def majorityElement(self, nums):
        count1=count2=max1=max2=0

        for i in range(len(nums)):
            if nums[i] == max1:
                count1+=1
            elif nums[i] == max2:
                count2+=1
            elif count1 == 0:
                count1 = 1
                max1 = nums[i]
            elif count2 == 0:
                count2 = 1
                max2 = nums[i]
            else:
                count1-=1
                count2-=1
        count1=count2=0
        for i in nums:
            if i == max1:
                count1+=1
            elif i == max2:
                count2+=1
        
        ans=[]
        if count1 > len(nums)//3:
            ans.append(max1)
        if count2 > len(nums)//3:
            ans.append(max2)
        return ans
    
