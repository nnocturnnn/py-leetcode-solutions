class Solution:
    def countTestedDevices(self, batteryPercentages: List[int]) -> int:
        def decrease_percent(bp):
            for i in range(len(bp)):
                bp[i] -= 1
            return 1
        return sum([decrease_percent(batteryPercentages) for i in batteryPercentages if i > 0])