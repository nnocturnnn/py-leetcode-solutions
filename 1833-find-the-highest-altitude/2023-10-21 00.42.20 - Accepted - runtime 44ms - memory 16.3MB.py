class Solution:
    def largestAltitude(self, gain: List[int]) -> int:
        gain.insert(0,0)
        attitude = [0] 
        for i in range(len(gain)):
            attitude.append(attitude[i] + gain[i])
        return max(attitude)
        