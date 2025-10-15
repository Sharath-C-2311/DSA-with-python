#my approach :

# class Solution:
#     def merge(self, intervals):
#         intervals.sort(key=lambda x:x[0])

#         ans=[]
#         i=0
#         j=0
#         while(i<len(intervals)-1):
#             sel=intervals[i][1]
#             j=i+1
#             while(j<len(intervals)):
#                 if sel >= intervals[j][0]:
#                     if intervals[j][1] > sel:
#                         sel = intervals[j][1]
#                     j+=1
#                 else:
#                     break    
#             ans.append([intervals[i][0],sel])
#             i += j-i
#         if j<len(intervals):
#             for i in range(j,len(intervals)):
#                 ans.append(intervals[i])
#         print(ans)
#         return ans


#similar approach

# class solution:
#     def merge(self,intervals):
#         intervals.sort(key=lambda x:x[0])
#         ans=[]
#         for i in range(len(intervals)):
#             start = intervals[i][0]
#             end = intervals[i][1]

#             if ans and end <= ans[-1][1]:
#                 continue

#             for j in range(i+1,len(intervals)):
#                 if end >= intervals[j][0]:
#                     end = max(end,intervals[j][1])
#                 else:
#                     break
#             ans.append([start,end])
#         return ans


#most optimal approach
class Solution:
    def merge(self, intervals):
        intervals.sort(key=lambda x:x[0])
        ans=[]
        for i in range(len(intervals)):

            if not ans or intervals[i][0] > ans[-1][1]:
                ans.append(intervals[i])

            else:
                ans[-1][1] = max(ans[-1][1],intervals[i][1])
        return ans
