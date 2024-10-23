class Solution:
    def findWords(self, words: List[str]) -> List[str]:
        fr, sr, tr = set("qwertyuiop"), set("asdfghjkl"), set("zxcvbnm")
        return [word for word in words if set(word.lower()).issubset(fr) 
                                    or set(word.lower()).issubset(sr) 
                                    or set(word.lower()).issubset(tr)]