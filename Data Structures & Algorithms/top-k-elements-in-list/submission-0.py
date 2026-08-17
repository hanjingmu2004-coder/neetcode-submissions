class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        cnt={}
        ans_temp=[1001]*(len(nums)+1)
        ans=[]
        for i in nums:
            if i not in cnt:
                cnt[i]=1
            else:
                cnt[i]+=1
        for key,value in cnt.items():
            ans_temp[value]=key
        for i in range(len(ans_temp)-1,-1,-1):
            if ans_temp[i]!=1001 and k!=0:
                ans.append(ans_temp[i])
                k-=1
                continue
            if k==0:
                return ans