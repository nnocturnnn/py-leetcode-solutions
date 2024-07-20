class Solution:
    def isPowerOfFour(self, n: int) -> bool:
        if n == 1:
            return True

        if n <= 0 or n & (n - 1) != 0:
            return False

        return n % 3 == 1
        