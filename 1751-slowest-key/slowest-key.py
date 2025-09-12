class Solution:
    def slowestKey(self, releaseTimes: List[int], keysPressed: str) -> str:
        max_dur = [releaseTimes[0]] + [b - a for a, b in zip(releaseTimes, releaseTimes[1:])]
        max_num = max(max_dur)
        result = [keysPressed[i] for i, num in enumerate(max_dur) if num == max_num and i < len(keysPressed)]
        return max(result)