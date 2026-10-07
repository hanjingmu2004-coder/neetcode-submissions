class Solution:
    def rob(self, nums: List[int]) -> int:
        n=len(nums)
        if n<3:
            return max(nums)
        if n==3:
            return max(nums[0]+nums[2],nums[1])
        dp=[0]*n
        dp[0],dp[1]=nums[0],nums[1]
        dp[2]=dp[0]+nums[2]
        for i in range(3,n):
            dp[i]=max(dp[i-2],dp[i-3])+nums[i]
        return max(dp[n-2],dp[n-1])