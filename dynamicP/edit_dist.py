class Solution:
    def minDistance(self, word1, word2):
        
        dp = [[0]*(len(word1)+1) for _ in range(len(word2)+1)]

        for i in range(len(word2)+1):
            for j in range(len(word1)+1):
                if i==0 or j==0:
                    dp[i][j] = i+j
                elif word1[j-1] == word2[i-1]:
                    dp[i][j] = dp[i-1][j-1]
                else:
                    dp[i][j] = 1+min(dp[i-1][j],dp[i][j-1],dp[i-1][j-1])
        for i in dp:
            print(i)     
        return dp[-1][-1]

# Given two strings word1 and word2, return the minimum number of operations required to convert word1 to word2.

# You have the following three operations permitted on a word:

# Insert a character
# Delete a character
# Replace a character

# Example 1:

# Input: word1 = "horse", word2 = "ros"
# Output: 3
# Explanation: 
# horse -> rorse (replace 'h' with 'r')
# rorse -> rose (remove 'r')
# rose -> ros (remove 'e')