from functools import reduce

class Solution:
    def subtractProductAndSum(self, n: int) -> int:
        prod_of_dig, sum_of_dig = 1, 0 
        while n > 0:
            digit = n % 10
                prod_of_dig *= digit
                sum_of_dig += digit
            n = n // 10
        return prod_of_dig - sum_of_dig