class Solution:
    def maximumGain(self, s: str, x: int, y: int) -> int:
        total_score = 0
        priority_pair, pair = ("ab", "ba") if x > y else ("ba", "ab")
        priority_score, pair_score = (x, y) if x > y else (y, x)

        while priority_pair in s or pair in s:
            if priority_pair in s:
                s = s.replace(priority_pair, "", 1)
                total_score += priority_score
            elif pair in s:
                s = s.replace(pair, "", 1)
                total_score += pair_score
        return total_score