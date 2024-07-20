class Solution:
    def countKeyChanges(self, s: str) -> int:
        s = s.lower()
        return sum([1 for i in range(len(s) - 1) if s[i] != s[i+1]])
            
            
