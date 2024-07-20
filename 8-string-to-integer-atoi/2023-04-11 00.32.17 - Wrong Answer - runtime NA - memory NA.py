import re

class Solution:
    def myAtoi(self, s: str) -> int:
        if match := re.search(r'^\s*([+-]?\d+)', s):
            num = int(match.group(1))
            if num > 0:
                return 2 ** 31 if num > 2 ** 31 else num
            else:
                return -2 ** 31 if num < -2 ** 31 else num
        
        else:
            return 0 