class Solution:
    def lemonadeChange(self, bills):
        five=0
        ten=0
        for i in bills:
            if i==5:
                five+=1
            elif i==10:
                five-=1
                ten+=1
            else:
                five-=1
                if ten > 0:
                    ten-=1
                else:
                    five-=2
            if five<0:
                return False
        return True
    
# Note that you do not have any change in hand at first.

# Given an integer array bills where bills[i] is the bill the ith customer pays,
# return true if you can provide every customer with the correct change, or false otherwise.

# Example 1:

# Input: bills = [5,5,5,10,20]
# Output: true
# Explanation: 
# From the first 3 customers, we collect three $5 bills in order.
# From the fourth customer, we collect a $10 bill and give back a $5.
# From the fifth customer, we give a $10 bill and a $5 bill.
# Since all customers got correct change, we output true.