class Solution:
    def longestCommonPrefix(self, strs):
        
        min_l=float('inf')
        for i in strs:
            if len(i) < min_l:
                min_l=len(i)
                min_str = i
        j=len(min_str)
        while(j>0):
            flag=0
            for i in strs:
                if min_str[0:j] not in i[0:j]:
                    flag=1
                    break
            if flag==0:
                return min_str[0:j]
            else:
                j-=1
        return ""
    
# Write a function to find the longest common prefix string amongst an array of strings.
# If there is no common prefix, return an empty string "".

# Example 1:

# Input: strs = ["flower","flow","flight"]
# Output: "fl"
# Example 2:

# Input: strs = ["dog","racecar","car"]
# Output: ""
# Explanation: There is no common prefix among the input strings.
