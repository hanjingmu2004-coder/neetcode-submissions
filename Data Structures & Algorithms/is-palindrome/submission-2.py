class Solution:
    def isPalindrome(self, s: str) -> bool:
        slist=[]
        for i in s.lower():
            if ord("a")<=ord(i)<=ord("z") or ord("0")<=ord(i)<=ord("9"):
                slist.append(i)
        l,r=0,len(slist)-1
        while l<r:
            if slist[l]!=slist[r]:
                return False
            else:
                l+=1
                r-=1
        return True