class Solution:
    def sortSentence(self, s: str) -> str:
        sentence = s.split()
        result = [0] * len(sentence)
        for i in sentence:
            result[int(i[-1]) - 1] = i[0:-1] 
        return " ".join(result)