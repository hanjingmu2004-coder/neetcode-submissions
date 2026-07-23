class Solution:
    def maxArea(self, heights: List[int]) -> int:
        ans=0
        l,r=0,len(heights)-1
        while l<r:
            ans=max(ans,min(heights[l],heights[r])*(r-l))
            if heights[l]>heights[r]:
                r-=1
            elif heights[l]<heights[r]:
                l+=1
            else:
                if heights[l+1]>=heights[r-1]:
                    l+=1
                else:
                    r-=1
        return ans