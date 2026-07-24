class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        l,ans=0,0
        cnt={}
        for r in range(len(s)):
            if s[r] not in cnt:
                cnt[s[r]]=1
            else:
                cnt[s[r]]+=1
            while len(cnt)>=2 and (sum(cnt.values())-max(cnt.values()))>k:
                cnt[s[l]]-=1
                if cnt[s[l]]==0:
                    del cnt[s[l]]
                l+=1
            ans=max(ans,r-l+1)
        return ans