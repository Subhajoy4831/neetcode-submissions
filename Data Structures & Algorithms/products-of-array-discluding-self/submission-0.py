class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        prefix = [0] * len(nums)
        suffix = [0] * len(nums)
        res = [0] * len(nums)
        for i,num in enumerate(nums):
            if i == 0:
                prefix[i] = num
            else:
                prefix[i] = prefix[i-1] * num
        
        for i in range(len(nums)-1,-1,-1):
            if i == len(nums)-1:
                suffix[i] = nums[i]
            else:
                suffix[i] = suffix[i+1] * nums[i]

        for i in range(0,len(nums)):
            if i == 0:
                res[i] = suffix[i+1]
            elif i == len(nums)-1:
                res[i] = prefix[i-1]
            else:
                res[i] = prefix[i-1] * suffix[i+1]
        
        return res