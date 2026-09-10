class Solution:
    def minWindow(self, s: str, t: str) -> str:
        res = [-1,-1]
        resLen = float("infinity")
        if len(t)>len(s):
            return ""

        mp,window = {},{}
        for i in range(len(t)):
            mp[t[i]] = mp.get(t[i],0)+1
        have, need = 0,len(mp)
        l = 0
        for r in range(len(s)):
            c = s[r]
            window[c] = 1 + window.get(c,0)
            if c in mp and mp[c] == window[c]:
                have+=1
            
            while have == need:
                if(r-l+1)<resLen:
                    resLen = r-l+1
                    res = [l,r]

                window[s[l]] -= 1
                if s[l] in mp and window[s[l]]<mp[s[l]]:
                    have-=1
                l+=1
        l,r = res
        return s[l:r+1] if resLen !=float("infinity") else ""