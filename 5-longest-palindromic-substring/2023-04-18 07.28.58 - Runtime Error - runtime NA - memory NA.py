class Solution:
    def longestPalindrome(self, s: str) -> str:
        modifiedString = "#".join("^{}$".format(string))
        n = len(modifiedString)
        P = [0] * n
        C = 0
        R = 0
        for i in range (1,n-1):
            if i < R:
                P[i] = min(R-i, P[2*C-i])
            
            # Attempt to expand palindrome centered at i
            while modifiedString[i + 1 + P[i]] == modifiedString[i - 1 - P[i]]:
                P[i] += 1
            
            # If palindrome centered at i expand past R,
            # adjust center based on expanded palindrome.
            if i + P[i] > R:
                C, R = i, i + P[i]
        
        # Find the maximum element in P.
        maxLen, centerIndex = max((n, i) for i, n in enumerate(P))
        return string[(centerIndex  - maxLen)//2:(centerIndex  + maxLen)//2]