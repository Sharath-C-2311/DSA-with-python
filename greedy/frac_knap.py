class Solution:
    def fractionalKnapsack(self, val, wt, cap):
        vw = []
        for i in range(len(val)):
            vw.append([val[i]/wt[i],val[i],wt[i]])
        vw.sort(key=lambda x:x[0],reverse=True)
        c=0
        result=0
        i=0
        while(c<cap and i<(len(vw))):
            print(c)
            if c+vw[i][2] < cap:
                c+=vw[i][2]
                result+=vw[i][1]
            else:
                result+=(cap-c)*vw[i][0]
                c+=(cap-c)
            i+=1
        return result
    

# Fractional Knapsack

# You have n items; the i-th item has value val[i] and weight wt[i].
# A knapsack can carry at most capacity units of weight.
# You may take any fraction of an item (i.e. split items).
# Return the maximum total value that can be placed in the knapsack, rounded to exactly 6 decimal places.


# Examples:
# Input: val = [60,100,120], wt = [10,20,30], capacity = 50

# Output: 240.000000

# Explanation:

#  • Take item 0 (w=10, v=60)

#  • Take item 1 (w=20, v=100)

#  • Take 2⁄3 of item 2 (w=20, v=80)

# Total value = 60 + 100 + 80 = 240