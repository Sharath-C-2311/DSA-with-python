class Solution:
    def findPlatform(self, Arrival, Departure):
        ref = Departure[0]
        comp = [0]*len(Arrival)
        comp[0]=1
        ans=1
        while True:
            n=0
            while n<len(Arrival):
                if Arrival[n] > ref and comp[n]==0:
                    ref = Departure[n]
                    comp[n]=1
                n+=1
            n=0
            flag=0
            while n<len(Arrival):
                if comp[n]==0:
                    flag=1
                    ans+=1
                    comp[n]=1
                    ref = Arrival[n]
                    break
                n+=1
            if flag==0:
                break
        return ans
    
#efficient method
def countPlatforms(arr, dep):
    arr.sort()
    dep.sort()

    ans = 1
    count = 1
    i = 1
    j = 0
    while i < len(arr) and j < len(dep):
        if arr[i] <= dep[j]:  # one more platform needed
            count += 1
            i += 1
        else:  # one platform can be reduced
            count -= 1
            j += 1
        ans = max(ans, count)  # updating the value with the current maximum
    return ans

# Given the arrival and departure times of all trains reaching a particular railway station,
#  determine the minimum number of platforms required so that no train is kept waiting. 
# Consider all trains arrive and depart on the same day.
# In any particular instance, the same platform cannot be used for both the departure of 
# one train and the arrival of another train, necessitating the use of different platforms
# in such cases.

# Note: Time intervals are in the 24-hour format (HHMM) , where the first two characters represent hour (between 00 to 23 ) and the last two characters represent minutes (this will be <= 59 and >= 0). Leading zeros for hours less than 10 are optional (e.g., 0900 is the same as 900).

# Examples:
# Input : Arrival = [900, 940, 950, 1100, 1500, 1800] , 
# Departure = [910, 1200, 1120, 1130, 1900, 2000]
# Output : 3

# Explanation : The first , second , fifth number train can use the platform 1.

# The third and sixth train can use the platform 2.
# The fourth train will use platform 3.
# So total we need 3 different platforms for the railway station so that no train is kept waiting.