class Solution:
    def buyChoco(self, prices: List[int], money: int) -> int:
        prices.sort()
        min_sum = float('inf')
        found = False

        for i in range(len(prices)):
            for j in range(i + 1, len(prices)):
                sum_prices = prices[i] + prices[j]

                if sum_prices <= money and sum_prices < min_sum:
                    min_sum = sum_prices
                    found = True

        return money - min_sum if found else money