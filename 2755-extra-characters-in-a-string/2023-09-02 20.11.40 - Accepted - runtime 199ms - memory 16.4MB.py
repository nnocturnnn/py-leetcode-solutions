class Solution:
    def minExtraChar(self, s: str, dictionary: List[str]) -> int:
        n = len(s) + 1
        dp = [n] * (len(s) + 1)
        dp[0] = 0
        ds = set(dictionary)

        for i in range(1, len(s) + 1):
            dp[i] = dp[i - 1] + 1
            for j in range(1, i + 1):
                if s[i - j: i] in ds:
                    dp[i] = min(dp[i], dp[i - j])


        return dp[-1]
        