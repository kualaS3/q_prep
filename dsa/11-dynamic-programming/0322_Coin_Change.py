class Solution:
    def coinChange(self, coins: list[int], amount: int) -> int:
        dp = [float('inf')] *( amount + 1) 
        dp[0] = 0
        for x in range(1, amount + 1): # iterate thru all indexes till amt
            for c in coins: # iterate thru all coin vals
                if c <= x: # avoid pointless indices 
                    dp[x] = min(dp[x], dp[x - c] + 1)
        return dp[amount] if dp[amount] != float('inf') else -1
