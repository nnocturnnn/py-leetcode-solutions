class Solution:
    def winnerOfGame(self, colors: str) -> bool:
        win = 0
        for i in range(1, len(colors) - 1):
            if colors[i-1:i+2] == "AAA":
                win += 1
            if colors[i-1:i+2] == "BBB":
                win -= 1
        return True if win > 0 else False
        

        