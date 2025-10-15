class Solution:
    def JobScheduling(self, jobs):
        jobs.sort(key=lambda x:x[2],reverse=True)

        maxi = jobs[0][1]
        for i in jobs:
            if i[1] > maxi:
                maxi = i[1]
        
        slot = [0]*(maxi)
        prof=0
        num = 0
        for i in range(len(jobs)):
            for j in range(jobs[i][1]-1,-1,-1):
                if slot[j] == 0:
                    slot[j]=1
                    prof+=jobs[i][2]
                    num+=1
                    break
        
        return [num,prof]
    

# Given an 2D array Jobs of size Nx3, where Jobs[i][0] represents JobID , Jobs[i][1] represents Deadline , 
# Jobs[i][2] represents Profit associated with that job. 
# Each Job takes 1 unit of time to complete and only one job can be scheduled at a time.
# The profit associated with a job is earned only if it is completed by its deadline. 
# Find the number of jobs and maximum profit.


# Examples:
# Input : Jobs = [ [1, 4, 20] , [2, 1, 10] , [3, 1, 40] , [4, 1, 30] ]

# Output : 2 60

# Explanation : Job with JobID 3 can be performed at time t=1 giving a profit of 40.

# Job with JobID 1 can be performed at time t=2 giving a profit of 20.

# No more jobs can be scheduled, So total Profit = 40 + 20 => 60.

# Total number of jobs completed are two, JobID 1, JobID 3.

# So answer is 2 60