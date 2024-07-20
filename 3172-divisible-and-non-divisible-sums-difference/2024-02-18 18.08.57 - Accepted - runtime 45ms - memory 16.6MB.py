class Solution:
    def differenceOfSums(self, n: int, m: int) -> int:
        div, non_div = [], []
        _ = [div.append(i) if i % m == 0 else non_div.append(i) for i in range(1, n + 1)]
        return sum(non_div) - sum(div)