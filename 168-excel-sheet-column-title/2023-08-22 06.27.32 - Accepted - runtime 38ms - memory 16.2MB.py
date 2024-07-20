class Solution:
    def convertToTitle(self, columnNumber: int) -> str:
        title = ""
        while columnNumber > 0:
            columnNumber -= 1
            rm = columnNumber % 26
            letter = chr(ord('A') + rm)
            title = letter + title
            columnNumber //= 26
        return title