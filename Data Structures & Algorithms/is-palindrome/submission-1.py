class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = s.lower()
        val = ""
        for c in s:
            if c.isalnum():
                val+=c
        for i in range(0,len(val)//2):
            if val[i] != val[len(val)-1-i]:
                return False
        return True