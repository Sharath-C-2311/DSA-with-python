class Solution:
    def lengthOfLongestSubstring(self, s):
        if s=="":
            return 0
        dic={}
        temp_s=""
        req=1
        for i in range(len(s)):
            if s[i] in dic:
                j=dic[s[i]]
                k=dic[temp_s[0]]
                if j>=k:
                    temp_s = s[j+1:i+1]
                else:
                    temp_s+=s[i]
            else:
                temp_s+=s[i]
            if len(temp_s)>req:
                    req=len(temp_s)
            dic[s[i]]=i
        return req


# 3. Longest Substring Without Repeating Characters
# Given a string s, find the length of the longest substring without duplicate characters.

# Example 1:

# Input: s = "abcabcbb"
# Output: 3
# Explanation: The answer is "abc", with the length of 3. Note that "bca" and "cab" are also correct answers.
