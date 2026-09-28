class Solution:
    def search(self, nums: List[int], target: int) -> int:
        if nums is None:
            return -1
        left = 0
        right = len(nums)-1
        nums.sort()
        while left<=right:
            mid = (left+right)//2
            if nums[mid] == target:
                return mid
            elif nums[mid]>target:
                right = mid-1
            elif nums[mid]<target:
                left = mid+1
        return -1