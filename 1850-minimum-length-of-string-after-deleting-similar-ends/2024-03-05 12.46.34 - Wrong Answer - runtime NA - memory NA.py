class Solution:
    def minimumLength(self, s: str) -> int:
        left, right = 0, len(s) - 1
        while left < right:
            buffer = s[left]
            while left < right and s[left] == buffer:
                left += 1
            while right > left and s[right] == buffer:
                right -= 1

        return right - left + 1 

