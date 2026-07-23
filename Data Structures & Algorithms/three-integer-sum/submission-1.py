class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        ans=[]
        nums.sort()
        for i in range(len(nums)-2):
            if i>=1 and nums[i]==nums[i-1]:
                i+=1
                continue
            target=-nums[i]
            j,k=i+1,len(nums)-1
            while j<k:
                if nums[j]+nums[k]<target:
                    j+=1
                elif nums[j]+nums[k]>target:
                    k-=1
                else:
                    ans.append([nums[i],nums[j],nums[k]])
                    while nums[k]==nums[k-1]:
                        if j>=k:
                            break
                        k-=1
                    k-=1
        return ans