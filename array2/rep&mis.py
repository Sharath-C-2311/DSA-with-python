#find both missing(only 1 element) and repeating(1 element repeated only 2 times) elements
# array of size "n" and elements starts from [1,n] note:elements starts from 1

class Solution:
    def findMissingRepeatingNumbers(self, nums):
        
        slow = nums[0]
        fast = nums[0]

        while True:
            slow = nums[slow]
            fast = nums[nums[fast]]

            if slow == fast:
                break
        
        fast = nums[0]

        while slow!=fast:
            slow = nums[slow]
            fast = nums[fast]
        repeat = slow

        n=len(nums)

        sum_of_n = n*(n+1)//2
        
        actual_sum = sum(nums)

        miss = sum_of_n - (actual_sum - repeat)

        return [repeat,miss]
