import sys
sys.set_int_max_str_digits(10**6)

class Solution:
    def addToArrayForm(self, num: List[int], k: int) -> List[int]:
        return list(map(int,list(str(int("".join(map(str, num))) + k))))