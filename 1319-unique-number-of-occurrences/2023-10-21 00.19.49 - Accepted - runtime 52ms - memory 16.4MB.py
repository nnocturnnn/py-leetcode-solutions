class Solution:
    def uniqueOccurrences(self, arr: List[int]) -> bool:
        numb_of_occur = [arr.count(i) for i in set(arr)]
        return len(numb_of_occur) == len(set(numb_of_occur))
        