class Solution:
    def plusOne(self, digits):
        flag=True
        i=len(digits)-1
        temp=0
        while flag and i>-1:
            temp = digits[i]+1
            if temp > 9:
                digits[i]=0
            else:
                digits[i]=temp
                flag=False
            i-=1
        if i==-1 and temp>9:
            arr = [1]
            arr.extend(digits)
            digits = arr
        return digits 
    
# 66. Plus One

# Example 1:

# Input: digits = [1,2,3]
# Output: [1,2,4]
# Explanation: The array represents the integer 123.
# Incrementing by one gives 123 + 1 = 124.
# Thus, the result should be [1,2,4].


# Example 2:

# Input: digits = [4,3,2,1]
# Output: [4,3,2,2]
# Explanation: The array represents the integer 4321.
# Incrementing by one gives 4321 + 1 = 4322.
# Thus, the result should be [4,3,2,2].


# Example 3:

# Input: digits = [9]
# Output: [1,0]
# Explanation: The array represents the integer 9.
# Incrementing by one gives 9 + 1 = 10.
# Thus, the result should be [1,0].