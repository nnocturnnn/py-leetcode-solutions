import re

class Solution:
    def myAtoi(self, s: str) -> int:
        if match := re.search(r'^\s*([+-]?\d+)', s):
            return int(match.group(1))
        else:
            return 0 