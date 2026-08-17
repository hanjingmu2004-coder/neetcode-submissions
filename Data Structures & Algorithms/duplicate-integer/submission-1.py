class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        cnt=defaultdict()
        for i in nums:
            if i in cnt:
                return false
            cnt[i]=1
        return true