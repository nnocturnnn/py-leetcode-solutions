class Solution:
    def backspaceCompare(self, s: str, t: str) -> bool:
        new_s, new_t = [], []
        for i in range(max([len(s), len(t)])):
            if i < len(s):
                new_s.pop() if s[i] == "#" and new_s and i < len(s) else new_s.append(s[i])
            if i < len(t):
                new_t.pop() if t[i] == "#" and new_t and i < len(t) else new_t.append(t[i])
        return new_s == new_t
            