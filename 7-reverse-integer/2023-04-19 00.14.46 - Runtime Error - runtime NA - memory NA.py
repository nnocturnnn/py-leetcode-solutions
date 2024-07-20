import re

class Solution:
    def reverse(self, x: int) -> int:
        if x > 2 ** 31 -1 or x < -2 ** 31:
            return 0
        x_str = str(x)
        count = 0
        r_zero = "0"
        while x_str.endswith(r_zero):
            r_zero += "0"
            count += 1
        x_str = re.sub(f'{"0" * count}$', '', x_str)
        if x < 0:
            return int(x_str[1:][::-1]) * -1
        else:
            return int(x_str[::-1])