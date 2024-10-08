
class Solution:
    def sequentialDigits(self, low: int, high: int) -> List[int]:
        all_seq = []
        seq = "123456789"

        for length in range(len(str(low)), len(str(high)) + 1):
            for start in range(0, 10 - length):
                num = int(seq[start:start + length])
                if low <= num <= high:
                    all_seq.append(num)
        return all_seq