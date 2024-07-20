class Solution:
    def frequencySort(self, s: str) -> str:
        final_str = str()
        sorted_letter_count = dict(sorted({i : s.count(i) for i in s}.items(), key=lambda item: item[1], reverse=True))
        for letter, count in sorted_letter_count.items():
            final_str += letter * count
        return final_str