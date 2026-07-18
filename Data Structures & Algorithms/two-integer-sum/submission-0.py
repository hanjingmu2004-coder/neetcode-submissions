class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        cnt={}
        for i in range(len(nums)):
            if target-nums[i] in cnt:
                return [cnt[target-nums[i]],i]
            cnt[nums[i]]=i
        return None