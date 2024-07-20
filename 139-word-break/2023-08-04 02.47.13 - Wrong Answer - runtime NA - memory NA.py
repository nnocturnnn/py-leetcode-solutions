class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        for i in wordDict:
            if i not in s:
                return False
            s = s.replace(i, "")
        return True