class Solution:
    def bestClosingTime(self, customers: str) -> int:
        max_score = score = 0
        best = -1
        for i, c in enumerate(customers):
            score += 1 if c == "Y" else -1
            if score > max_score:
                max_score, best = score, i
        return best + 1