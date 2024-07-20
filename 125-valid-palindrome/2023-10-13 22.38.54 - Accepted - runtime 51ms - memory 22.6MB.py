class Solution:
    def isPalindrome(self, s: str) -> bool:
        alphanum = [i.lower() for i in s if i.isalnum()]
        return alphanum == alphanum[::-1]
        