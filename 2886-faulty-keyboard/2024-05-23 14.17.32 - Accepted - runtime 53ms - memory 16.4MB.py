class Solution:
    def finalString(self, s: str) -> str:
        output = ""
        for char in s:
            if char == "i":
                output = output[::-1]
            else:
                output += char
        return output