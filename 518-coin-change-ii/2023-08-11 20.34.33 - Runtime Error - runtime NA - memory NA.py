from itertools import combinations 

class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        coin_combo = [0] * (amount + 1)
        coin_combo[0] = 1
        for coin in coins:
            for i in range(coin, amount + 1):
                coin_combo[i] += coin_combo[i - coin]

        return coin_combo[i]
        