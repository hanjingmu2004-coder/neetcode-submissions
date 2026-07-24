class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        k=len(s1)
        cnt_1=Counter(s1)
        l,r=0,0
        cnt={}
        while r<len(s2):
            if r<k-1:
                if s2[r] not in cnt:
                    cnt[s2[r]]=1
                else:
                    cnt[s2[r]]+=1
                r+=1
            else:
                if s2[r] not in cnt:
                    cnt[s2[r]]=1
                else:
                    cnt[s2[r]]+=1
                if cnt==cnt_1:
                    return True
                cnt[s2[l]]-=1
                if cnt[s2[l]]==0:
                    del cnt[s2[l]]
                l+=1
                r+=1
        return False