class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        dic={
            "2":"abc",
            "3":"def",
            "4":"ghi",
            "5":"jkl",
            "6":"mno",
            "7":"pqrs",
            "8":"tuv",
            "9":"wxyz"
        }

        ans=[]

        def solve(i,letters):
            if i==len(digits):
                ans.append(letters)
                return
            
            for j in dic[digits[i]]:
                solve(i+1,letters+j)
        
        solve(0,"")

        return ans

# 17. Letter Combinations of a Phone Number

# Given a string containing digits from 2-9 inclusive, 
# return all possible letter combinations that the number could represent. 
# Return the answer in any order

# Example 1:

# Input: digits = "23"
# Output: ["ad","ae","af","bd","be","bf","cd","ce","cf"]

# Example 2:

# Input: digits = "2"
# Output: ["a","b","c"]