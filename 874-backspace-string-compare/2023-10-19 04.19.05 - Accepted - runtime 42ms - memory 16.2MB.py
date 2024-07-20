class Solution:
    def backspaceCompare(self, s: str, t: str) -> bool:
        new_s, new_t = [], []
        for i in range(max([len(s), len(t)])):
            if i < len(s):
                if s[i] == "#" and new_s:
                    new_s.pop()
                elif s[i] != "#":
                    new_s.append(s[i])
            
            if i < len(t):
                if t[i] == "#" and new_t:
                    new_t.pop()
                elif t[i] != "#":
                    new_t.append(t[i])

        return new_s == new_t
                