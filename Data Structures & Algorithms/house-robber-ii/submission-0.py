class Solution:
    def rob(self, nums: List[int]) -> int:
        n=len(nums)
        dp=[0]*(n-1)
        dp_p=[0]*(n-1)
        if n<=3:
            return max(nums)
        dp[0],dp[1]=nums[0],nums[1]
        dp_p[0],dp_p[1]=nums[1],nums[2]
        for i in range(2,n-1):
            if i==2:
                dp[i],dp_p[i]=dp[i-2]+nums[i],dp_p[i-2]+nums[i+1]
            else:
                dp[i]=max(dp[i-2],dp[i-3])+nums[i]
                dp_p[i]=max(dp_p[i-2],dp_p[i-3])+nums[i+1]
        return max(max(dp),max(dp_p))