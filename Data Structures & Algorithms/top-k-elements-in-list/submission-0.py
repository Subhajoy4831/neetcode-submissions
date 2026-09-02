class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        hashmap = {}
        res = []
        for i,num in enumerate(nums):
            hashmap[num] = hashmap.get(num,0)+1
        length = len(nums) + 1
        arr = [[] for _ in range(length)]
        for n,c in hashmap.items():
            arr[c].append(n)
        for i in range(length-1,0,-1):
            for n in arr[i]:
                res.append(n)
                if len(res) == k:
                    return res
        return res