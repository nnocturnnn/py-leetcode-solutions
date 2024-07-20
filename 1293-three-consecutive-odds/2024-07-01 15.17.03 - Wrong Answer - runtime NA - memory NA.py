class Solution:
    def threeConsecutiveOdds(self, arr: List[int]) -> bool:
        for i in range(len(arr) - 2):
            f, s, t = arr[i], arr[i + 1], arr[i + 2]
            if f <= s <= t:
                if f % 2 == 0 and s % 2 == 0 and t % 2 ==0:
                    return True
        return False