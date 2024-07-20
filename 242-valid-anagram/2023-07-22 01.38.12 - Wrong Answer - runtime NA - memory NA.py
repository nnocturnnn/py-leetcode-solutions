class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) > len(t):
            return False
        a_sum = 0
        b_sum = 0
        for f, s in zip(s, t):
            a_sum += hash(f)
            b_sum += hash(s)
        return True if a_sum == b_sum else False