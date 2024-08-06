class Solution:
    def sumZero(self, n: int) -> List[int]:
        num =  n // 2
        sumz = [i for i in range(-num,num + 1,1)] if n % 2 != 0 else [i for i in range(-num, num + 1,1) if i != 0]
        return sumz