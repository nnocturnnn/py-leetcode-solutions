class Solution:
    def myPow(self, base: float, exponent: int) -> float:
        if exponent == 0:
            return 1

        if exponent < 0:
            base = 1 / base
            exponent = -exponent

        result = 1
        while exponent > 0:
            if exponent % 2 == 1:
                result *= base
            base *= base
            exponent //= 2

        return result