class Solution:
    def longestPalindrome(self, s: str) -> str:
        t = '#'.join('^{}$'.format(s))
        n = len(t)
        P = [0] * n
        C = 0
        R = 0

        for i in range(1, n - 1):
            if i < R:
                P[i] = min(R - i, P[2 * C - i])
            else:
                P[i] = 0

            while t[i + P[i] + 1] == t[i - P[i] - 1]:
                P[i] += 1

            if i + P[i] > R:
                C = i
                R = i + P[i]

        max_length = max(P)
        center = P.index(max_length)

        longest_palindrome = t[center - max_length: center + max_length + 1].replace('#', '')

        return longest_palindrome