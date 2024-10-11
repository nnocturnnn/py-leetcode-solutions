class Solution:
    def secondHighest(self, s: str) -> int:
        digits = set()
        [digits.add(i) for i in s if i.isdigit()]
        lst_digits = list(digits)
        lst_digits.sort()
        if len(digits) > 1:
            return int(lst_digits[-2])
        return -1