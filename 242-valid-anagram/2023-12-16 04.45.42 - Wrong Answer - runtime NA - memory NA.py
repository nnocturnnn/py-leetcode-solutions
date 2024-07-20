class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return 0 
        anagram = 0
        for k, i in zip(s, t):
            anagram += ord(k)
            anagram -= ord(i)
        return not anagram
