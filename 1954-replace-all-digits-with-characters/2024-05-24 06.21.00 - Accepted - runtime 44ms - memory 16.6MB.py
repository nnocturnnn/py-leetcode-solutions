class Solution:
    def replaceDigits(self, s: str) -> str:
        out = ""
        for i in range(0, len(s), 2):
            out += s[i]  
            if i + 1 < len(s):
                out += chr(ord(s[i]) + int(s[i + 1]))
        return out