class Solution:
    @cache
    def climbStairs(self, n: int) -> int:
        if n<=2: return n
            return climbStairs(self,n-1)+climbStairs(self,n-2)
        