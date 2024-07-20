class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        ln = 0
        br = False
        for i in range(len(min(strs, key=len))):
            if len(set([strs[k][i] for k in range(len(strs))])) == 1:
                ln += 1
            else:
                break
        return strs[0][0:ln]