import collections

class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        result = collections.Counter(magazine)
        for i in ransomNote:
            if result[i] == 0:
                return False
            else:
                result[i] -= 1
        return True