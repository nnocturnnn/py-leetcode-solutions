class Solution:
    def reverseString(self, s: List[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        """
        def reverse(lo,hi):
            if lo > hi: return
            s[lo], s[hi] = s[hi], s[lo]
            reverse(lo+1, hi-1)
        reverse(0, len(s)-1)
        