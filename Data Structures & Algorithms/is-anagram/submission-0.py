class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        s_length = len(s)
        t_length = len(t)
        hashmap_s = {}
        hashmap_t = {}
        if s_length != t_length:
            return False
        for char in s:
            hashmap_s[char] = hashmap_s.get(char,0)+1
        for char in t:
            hashmap_t[char] = hashmap_t.get(char,0)+1
        for key in hashmap_s.keys():
            if hashmap_s[key] != hashmap_t.get(key,0):
                return False
        return True