class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hashmap = {}
        result = []
        for i,num in enumerate(nums):
            value = target - num
            if value in hashmap:
                result.append(hashmap[value])
                result.append(i)
            hashmap[num] = i
        return result
