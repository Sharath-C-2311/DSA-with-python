class Solution:
    def maxRunTime(self, n, batteries):
        total = sum(batteries)//n
        l,r=0,total

        while(l<r):
            m=(l+r+1)//2
            if sum(min(b,m) for b in batteries) >= n*m:
                l=m
            else:
                r=m-1
        return l
    
# 2141. Maximum Running Time of N Computers

# Input: n = 2, batteries = [3,3,3]
# Output: 4
# Explanation: 
# Initially, insert battery 0 into the first computer and battery 1 into the second computer.
# After two minutes, remove battery 1 from the second computer and insert battery 2 instead. Note that battery 1 can still run for one minute.
# At the end of the third minute, battery 0 is drained, and you need to remove it from the first computer and insert battery 1 instead.
# By the end of the fourth minute, battery 1 is also drained, and the first computer is no longer running.
# We can run the two computers simultaneously for at most 4 minutes, so we return 4.