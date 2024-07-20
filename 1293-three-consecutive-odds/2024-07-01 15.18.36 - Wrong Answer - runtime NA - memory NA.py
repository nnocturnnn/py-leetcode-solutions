class Solution:
    def threeConsecutiveOdds(self, arr: List[int]) -> bool:
        for i in range(len(arr) - 2):
            f, s, t = arr[i], arr[i + 1], arr[i + 2]
            if f <= s <= t:
                if f % 2 == 1 and s % 2 == 1 and t % 2 == 1:
                    return True
        return False