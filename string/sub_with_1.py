class Solution:
    def numSub(self, s):
        res=0
        count=0
        mod = 10**9+7
        for i in range(len(s)):
            if s[i] == "1":
                count+=1
            else:
                if count > 0:
                    res+=(count*(count+1)//2)
                count=0
        if count > 0:
            res+=(count*(count+1)//2)

        return res%mod

# Number of Substrings With Only 1s
# Given a binary string s, return the number of substrings with all characters 1's. Since the answer may be too large, return it modulo 109 + 7.

# Example 1:

# Input: s = "0110111"
# Output: 9
# Explanation: There are 9 substring in total with only 1's characters.
# "1" -> 5 times.
# "11" -> 3 times.
# "111" -> 1 time.

# Example 2:

# Input: s = "101"
# Output: 2
# Explanation: Substring "1" is shown 2 times in s.
