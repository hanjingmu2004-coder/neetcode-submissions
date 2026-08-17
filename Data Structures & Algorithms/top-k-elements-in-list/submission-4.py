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
            if ans_temp[value] is not list and ans_temp[value]!=1001:
                ans_temp[value]=[key,ans_temp[value]]
            if ans_temp[value] is list:
                ans_temp[value].append(key)
            if ans_temp[value]==1001:
                ans_temp[value]=key
        for i in range(len(ans_temp)-1,-1,-1):
            if ans_temp[i]!=1001 and k!=0:
                ans.append(ans_temp[i])
                k-=1 if ans_temp[i] is not list else len(ans_temp[i])
                continue
            if k==0:
                return ans