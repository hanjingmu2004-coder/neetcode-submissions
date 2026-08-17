class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        ans=[]
        cnt=[]
        if len(strs)==0:
            return [[""]]        
        for i in range(len(strs)):
            cnt_temp={}
            for c in strs[i]:
                if c not in cnt_temp:
                    cnt_temp[c]=1
                else:
                    cnt_temp[c]+=1
            cnt.append(cnt_temp)
            for j in range(len(cnt)):
                if cnt[j]==cnt_temp and j!=len(cnt)-1:
                    ans[j].append(strs[i])
                    break
                if j==len(cnt)-1:
                    ans.append([strs[i]])
        return ans