class Solution:
    def findDuplicate(self, nums):
        #time -> n , space -> constant
        slow = nums[0]
        fast = nums[0]
        while True:
            slow = nums[slow]
            fast  = nums[nums[fast]]
            if fast == slow:
                break
        fast = nums[0]
        while slow!=fast:
            slow = nums[slow]
            fast = nums[fast]
            
        return slow
    
    # class Solution:
    # def findDuplicate(self, nums: List[int]) -> int:
    #     time -> n , space -> n
    #     n=len(nums)
    #     arr=[0]*n
    #     for i in nums:
    #         if arr[i]==-1:
    #             return i
    #         arr[i]=-1
    #     return -1
        

    
