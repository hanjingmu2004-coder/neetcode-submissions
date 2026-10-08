class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        n=amount
        dp=[0]*(n+1)
        for i in range(1,n+1):
            cnt=10001
            for j in range(len(coins)):
                if i>=coins[j] and dp[i-coins[j]]!=-1:
                    cnt=min(dp[i-coins[j]],cnt)
            if cnt==10001:
                dp[i]=-1
            else:
                dp[i]=cnt+1
        return dp[n]