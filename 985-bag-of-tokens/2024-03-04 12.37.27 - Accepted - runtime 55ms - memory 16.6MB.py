class Solution:
    def __init__(self):
        self.score = 0

    def sell(self, power: int, token: int) -> int:
        self.score += 1
        return power - token

    def buy(self, power: int, token: int) -> int:
        self.score -= 1
        return power + token
    
    def bagOfTokensScore(self, tokens: List[int], power: int) -> int:
        tokens.sort()
        left, right = 0, len(tokens) - 1
        for _ in tokens:
            if left <= right:
                if tokens[left] <= power:
                    power = self.sell(power, tokens[left])
                    left += 1
                elif self.score > 0 and left < right:
                    power = self.buy(power, tokens[right])
                    right -= 1
                else:
                    break
            else:
                break 
        return self.score