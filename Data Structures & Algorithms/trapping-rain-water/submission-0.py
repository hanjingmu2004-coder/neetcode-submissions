class Solution:
    def trap(self, height: List[int]):
        l=[0]*len(height)
        r=[0]*len(height)
        l_m,r_m=0,0
        for i in range(len(height)):
            l_m=max(height[i],l_m)
            l[i]=l_m
        for i in range(len(height)-1,-1,-1):
            r_m=max(height[i],r_m)
            r[i]=r_m
        ans=0
        for i in range(len(height)):
            if min(l[i],r[i])>height[i]:
                ans+=min(l[i],r[i])-height[i]
        return ans
