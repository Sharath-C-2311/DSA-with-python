class Solution:
    def isSubsequence(self, s,t):
        j=0
        if s=="":
            return True
        for i in t:
            if s[j] == i:
                print(s[j],i)
                j+=1
                if(j==len(s)):
                    return True
        return False