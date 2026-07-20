class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        cnt={}
        ans=[]
        for i in nums:
            if i not in cnt:
                cnt[i]=1
            else:
                cnt[i]+=1
        tmp=[[] for _ in range(len(nums)+1)]
        for key,value in cnt.items():
            tmp[value].append(key)
        for i in range(len(tmp)-1,-1,-1):
            if tmp[i] is not None and k!=0:
                ans.extend(tmp[i])
                k-=len(tmp[i])
            if k==0:
                return ans