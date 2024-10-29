class Solution:
    def sumBase(self, n: int, k: int) -> int:
        base_k_sum = 0
        while n > 0:
            base_k_sum += n % k
            n //= k
        
        return base_k_sum