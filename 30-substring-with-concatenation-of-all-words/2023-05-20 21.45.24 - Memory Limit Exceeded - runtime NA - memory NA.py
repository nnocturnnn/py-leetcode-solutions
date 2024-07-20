from itertools import permutations

def find_all_indices(string, substring):
    start_index = 0
    while True:
        index = string.find(substring, start_index)
        if index == -1:
            return
        yield index
        start_index = index + 1

class Solution:
    def findSubstring(self, s: str, words: List[str]) -> List[int]:
        all_subs = ["".join(i) for i in permutations(words, len(words))]
        indexes = []
        for i in all_subs:
            if all_ind := find_all_indices(s, i):
                indexes += all_ind
        return set(indexes)