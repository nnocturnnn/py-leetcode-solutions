class Solution:
    def get_all_substrings(self, string: str):
        n = len(string)
        for i in range(n):
            yield string[i]
            for j in range(i + 1, n):
                yield string[i:j+1]

    
    def longestPalindrome(self, s: str) -> str:
        pal_dict = {len(i) : i for i in self.get_all_substrings(s) if i == i[::-1]}
        return pal_dict[max(pal_dict)]
        