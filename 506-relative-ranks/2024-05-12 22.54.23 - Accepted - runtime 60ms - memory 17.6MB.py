class Solution:

    def number_to_words(self, num):
        num_words = {
            1: "Gold Medal", 2: "Silver Medal", 3: "Bronze Medal"
        }
        return num_words.get(num, str(num))

    def custom_enumerate(self, iterable, start=1):
        count = start
        for item in iterable:
            yield self.number_to_words(count), item
            count += 1


    def findRelativeRanks(self, score: List[int]) -> List[str]:
        cd = {i : ite for ite ,i in self.custom_enumerate(sorted(score, reverse=True))}
        return [cd[i] for i in score]