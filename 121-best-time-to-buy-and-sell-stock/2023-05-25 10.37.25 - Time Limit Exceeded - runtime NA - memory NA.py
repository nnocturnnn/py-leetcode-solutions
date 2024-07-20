class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        profit_list = [0]
        for i in range(len(prices)):
            temp_profit = [0]
            for k in range(i + 1, len(prices)):
                temp_profit.append(prices[k] - prices[i])
            profit_list.append(max(temp_profit))
        return max(profit_list)