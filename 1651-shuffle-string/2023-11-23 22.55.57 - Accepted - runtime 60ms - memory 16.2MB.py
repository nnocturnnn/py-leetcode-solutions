class Solution:
    def restoreString(self, s: str, indices: List[int]) -> str:
        out = [None] * len(s)
        for letter, indice in zip(s, indices):
            out[indice] = letter
        return "".join(out)