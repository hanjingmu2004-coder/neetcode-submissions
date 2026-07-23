class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        l=0
        ans=0
        cnt={}
        for r in range(len(s)):
            while s[r] in cnt:
                del cnt[s[l]]
                l+=1
            cnt[s[r]]=1
            ans=max(r-l+1,ans)
        return ans