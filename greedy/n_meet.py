class Solution:
    def maxMeetings(self, start, end):
        arr = []
        for i in range(len(start)):
            arr.append([start[i],end[i],i])
        
        arr.sort(key=lambda x:(x[1],x[2]))
        
        prev = arr[0][1]
        count = 1
        for i in range(1,len(arr)):
            if arr[i][0] > prev:
                prev = arr[i][1]
                count+=1
        return count
    

# Given one meeting room and N meetings represented by two arrays, 
# start and end, where start[i] represents the start time of the ith meeting and end[i] 
# represents the end time of the ith meeting, determine the maximum number of meetings
#  that can be accommodated in the meeting room if only one meeting can be held at a time.

# Examples:
# Input : Start = [1, 3, 0, 5, 8, 5] , End = [2, 4, 6, 7, 9, 9]
# Output : 4

# Explanation : The meetings that can be accommodated in meeting room are (1,2) , (3,4) , (5,7) , (8,9)