class Solution:
    def countBits(self, n: int) -> List[int]:
        return [sum(map(int,"{0:b}".format(number))) for number in range(n + 1)]

        
        