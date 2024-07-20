import string

class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        max_count = 0
        start = 0
        chars = set()
        for end in range(len(s)):
            while s[end] in chars:
                chars.remove(s[start])
                start += 1
            chars.add(s[end])
            max_count = max(max_count, end - start + 1)
        return max_count



        