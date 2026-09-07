class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        l = 0
        hashmap = {}
        res = 0
        for r in range(len(s)):
            if s[r] in hashmap:
                l = max(l,hashmap[s[r]]+1)
            hashmap[s[r]] = r
            res = max(res, r-l+1)
        return res