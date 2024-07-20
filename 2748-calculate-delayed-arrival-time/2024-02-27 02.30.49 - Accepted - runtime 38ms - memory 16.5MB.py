class Solution:
    def findDelayedArrivalTime(self, arrivalTime: int, delayedTime: int) -> int:
        time =  arrivalTime + delayedTime
        answer = time if time < 24 else time % 24
        return answer
        