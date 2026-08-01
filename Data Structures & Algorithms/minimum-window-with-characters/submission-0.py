class Solution:
    def minWindow(self, s: str, t: str) -> str:
        ans_l,ans_r=-500,501
        l=0
        cnt_t=Counter(t)
        for r in range(len(s)):
            if s[r] in cnt_t:
                cnt_t[s[r]]-=1
            while max(cnt_t.values())==0:
                if ans_r-ans_l>r-l:
                    ans_l,ans_r=l,r
                if s[l] in cnt_t:
                    cnt_t[s[l]]+=1
                l+=1
        return s[ans_l:ans_r+1] if ans_r-ans_l<1001 else ""