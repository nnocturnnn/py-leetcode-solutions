class Solution:
    def getWinner(self, arr: List[int], k: int) -> int:
        n = len(arr)
        winner = arr[0]
        round_count = 0
        if k >= n:
            return max(arr)
        else:
            for i in range(1, n):
                if arr[i] > winner:
                    winner = arr[i]
                    round_count = 1
                else:
                    round_count += 1
                if round_count == k:
                    return winner
            return winner



        