class Solution:
    def get_all_substrings(self, string: str):
        n = len(string)
        for i in range(n):
            yield string[i]
            for j in range(i + 1, n):
                yield string[i:j+1]

    
    def longestPalindrome(self, s: str) -> str:
        longest_palindrome = ""
        max_length = 0
        
        for substr in self.get_all_substrings(s):
            if substr == substr[::-1] and len(substr) > max_length:
                max_length = len(substr)
                longest_palindrome = substr
        
        return longest_palindrome
        