class Solution:
    def productExceptSelf(self, nums: List[int]):
        ans=[]
        tmp=[]
        t=1
        m=nums[0]
        for i in range(len(nums)-1,0,-1):
           t=t*nums[i]
           tmp.append(t)
        tmp=tmp[::-1]
        ans.append(tmp[0])
        for i in range(1,len(nums)-1):
            ans.append(m*tmp[i])
            m=m*nums[i]
        ans.append(m)
        return ans