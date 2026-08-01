class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        l=0
        ans=[]
        cnt={}
        for r in range(len(nums)):
            if nums[r] not in cnt:
                cnt[nums[r]]=1
            else:
                cnt[nums[r]]+=1
            if r-l+1>k:
                cnt[nums[l]]-=1
                if cnt[nums[l]]==0:
                    del cnt[nums[l]]
                l+=1
            if r-l+1==k:
                ans.append(max(cnt.keys()))
        return ans