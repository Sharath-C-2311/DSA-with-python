
#20. Valid Parentheses

class Solution:
    def isValid(self, s):

        dic={")":"(","}":"{","]":"["}

        stack=[]

        for i in s:
            if i in dic:
                if not stack or dic[i] != stack[-1]:
                    return False
                stack.pop()
            else:
                stack.append(i)
        if len(stack) != 0:
            return False
        return True
    
