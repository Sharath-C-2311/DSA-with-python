class Solution:
    def longestCommonSubsequence(self, text1, text2):
        prev = [0]*(len(text2)+1)
        cur = [0]*(len(text2)+1)

        count=0
    
        for i in range(1,len(text1)+1):
            for j in range(1,len(text2)+1):
                if text1[i-1]==text2[j-1]:
                    cur[j]=1+prev[j-1]
                else:
                    cur[j] = max(cur[j-1],prev[j])
            prev = cur[:]
    
        return prev[-1]
    

# Given two strings text1 and text2, return the length of their longest common subsequence. 
# If there is no common subsequence, return 0.

# A subsequence of a string is a new string generated from the original string with 
# some characters (can be none) deleted without changing the relative order of the 
# remaining characters.

# For example, "ace" is a subsequence of "abcde".
# A common subsequence of two strings is a subsequence that is common to both strings.

# Example 1:

# Input: text1 = "abcde", text2 = "ace" 
# Output: 3  
# Explanation: The longest common subsequence is "ace" and its length is 3