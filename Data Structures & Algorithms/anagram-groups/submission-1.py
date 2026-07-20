class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        ans=[]
        cnt=[]    
        for i in range(len(strs)):
            cnt_temp={}
            for c in strs[i]:
                if c not in cnt_temp:
                    cnt_temp[c]=1
                else:
                    cnt_temp[c]+=1
            if i==0:
                ans.append([strs[i]])
                cnt.append(cnt_temp)
                continue
            for j in range(len(cnt)):
                if cnt[j]==cnt_temp:
                    ans[j].append(strs[i])
                    break
                if cnt[j]!=cnt_temp and j==len(cnt)-1:
                    ans.append([strs[i]])
                    cnt.append(cnt_temp)
        return ans