class Solution:
    def canPlaceFlowers(self, flowerbed: List[int], n: int) -> bool:
        for i in range(len(flowerbed) - 2):
            if flowerbed[i:i+3] == [0, 0, 0]:
                n -= 1
        
        return n <= 0
