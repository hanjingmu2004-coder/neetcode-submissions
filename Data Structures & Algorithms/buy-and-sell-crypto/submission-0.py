class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        ans=0
        l_min=101
        for i in range(len(prices)):
            l_min=min(l_min,prices[i])
            ans=max(ans,prices[i]-l_min)
        return ans