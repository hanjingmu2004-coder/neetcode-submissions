class Solution:
    def findMin(self, nums: List[int]) -> int:
        l,r=0,len(nums)-1
        if nums[0]<nums[-1]:
            return nums[0]
        ans=nums[-1]
        while l<=r:
            mid=(l+r)//2
            if nums[mid]>ans:
                l=mid+1
            if nums[mid]<=ans:
                ans=nums[mid]
                r=mid-1
            # if nums[mid]==ans:
            #     return ans
        return ans
