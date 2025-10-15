class Solution:
    def MinimumCoins(self, coins, amount):
        num=[float('inf')]*(amount+1)
        num[0]=0
        coins.sort(reverse=True)
        for i in range(1,amount+1):
            for coin in coins:
                if i-coin >= 0:
                    num[i] = min(num[i],num[i-coin]+1)
        return num[-1] if num[-1]!=float('inf') else -1
    

# Given an integer array of coins representing coins of different denominations 
# and an integer amount representing a total amount of money. 
# Return the fewest number of coins that are needed to make up that amount.
#  If that amount of money cannot be made up by any combination of the coins, return -1.
#  There are infinite numbers of coins of each type

# Examples:
# Input: coins = [1, 2, 5], amount = 11

# Output: 3

# Explanation: 11 = 5 + 5 + 1. We need 3 coins to make up the amount 11
