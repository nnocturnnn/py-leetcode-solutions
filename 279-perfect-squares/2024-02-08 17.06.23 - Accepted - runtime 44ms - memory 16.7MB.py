class Solution:
    def numSquares(self, n: int) -> int:
        if int(n**0.5) ** 2 == n:
            return 1
    
        for i in range(1, int(n**0.5) + 1):
            if int((n - i**2)**0.5) ** 2 == (n - i**2):
                return 2
    
        while n % 4 == 0:
            n /= 4
        if n % 8 == 7:
            return 4
        return 3