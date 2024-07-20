class Solution:
    def maximumGain(self, s: str, x: int, y: int) -> int:
        total_score = 0
        priority_pair, pair = ("ab", "ba") if x > y else ("ba", "ab")
        priority_score, pair_score = (x, y) if x > y else (y, x)

        def process_stack(s: str, first: str, second: str, score: int) -> (str, int):
            stack = []
            score_total = 0
            for char in s:
                if stack and stack[-1] == first and char == second:
                    stack.pop()
                    score_total += score
                else:
                    stack.append(char)
            return "".join(stack), score_total

        while priority_pair in s or pair in s:
            if priority_pair in s:
                s, score_high = process_stack(s, priority_pair[0], priority_pair[1], priority_score)
                total_score += score_high
            elif pair in s:
                s, score_low = process_stack(s, pair[0], pair[1], pair_score)
                total_score += score_low

        return total_score