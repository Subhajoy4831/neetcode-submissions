class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        res = []
        nums.sort()
        for i,num in enumerate(nums):
            if num > 0:
                break
            if i>0 and num == nums[i-1]:
                continue
            val = []
            l = i+1
            r = len(nums)-1
            while l<r:
                if nums[l]+nums[r] == -nums[i]:
                    res.append([num,nums[l],nums[r]])
                    l+=1
                    
                    while nums[l]==nums[l-1] and l<r:
                        l+=1
                elif nums[l]+nums[r] > -nums[i]:
                    r-=1
                elif nums[l]+nums[r] < -nums[i]:
                    l+=1
        return res    