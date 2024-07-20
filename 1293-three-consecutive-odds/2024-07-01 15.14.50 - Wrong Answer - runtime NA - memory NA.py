class Solution:
    def threeConsecutiveOdds(self, arr: List[int]) -> bool:
        for i in range(len(arr) - 2):
            print(arr[i])
            print(arr[i + 1])
            print(arr[i + 2])
            print("")
            if arr[i] <= arr[i + 1] <= arr[i + 2]:
                return True
        return False