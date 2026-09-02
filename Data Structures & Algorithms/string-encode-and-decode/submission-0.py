class Solution:

    def encode(self, strs: List[str]) -> str:
        res_s=""
        for s in strs:
            res_s += str(len(s))+"#"+s
        return res_s
    def decode(self, s: str) -> List[str]:
        res = []
        i = 0
        res_s = ""
        
        while i < len(s):
            s_num = ""
            while s[i] != "#":
                s_num += s[i]
                i+=1
            if  s[i] == "#":
                num = int(s_num)
                res_s = s[i+1:i+1+num]
                res.append(res_s)
                i+=num+1
        return res