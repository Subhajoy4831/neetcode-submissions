class Solution:
    def isValid(self, s: str) -> bool:
        check = []
        pair = {
            ")":"(",
            "}":"{",
            "]":"["
        }
        for c in s:
            if c in pair:
                if check and check[-1]==pair[c]:
                    check.pop()
                else:
                    return False
            else:
                check.append(c)
        return True if not check else False