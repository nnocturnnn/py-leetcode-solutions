import re

class Solution:
    def reverseParentheses(self, s: str) -> str:
        split_str = s.replace(")","(").split("(")[1:-1]
        mid = len(split_str) // 2
        final_str = split_str[mid]
        for i in range(mid + 1):
            if i != 0:
                final_str = final_str[::-1] 
                final_str = split_str[mid - i] + final_str + split_str[mid + i]
        return final_str[::-1]