class Solution:
    def canPlaceFlowers(self, flowerbed: List[int], n: int) -> bool:
        nextallow = True
        for i in range(len(flowerbed) - 2):
            if flowerbed[i:i+3] == [0, 0, 0] and nextallow:
                n -= 1
                nextallow = False
            else:
                nextallow = True

        return n <= 0
