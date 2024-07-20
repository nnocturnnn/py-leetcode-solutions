class Solution:
    def backspaceCompare(self, s: str, t: str) -> bool:
        new_s, new_t = [], []
        for i_s, i_t in zip(s, t):
            new_s.pop() if i_s == "#" and new_s else new_s.append(i_s)
            new_t.pop() if i_t == "#" and new_t else new_t.append(i_t)
        return new_s == new_t
            