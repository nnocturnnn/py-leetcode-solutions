class Solution:
    def averageWaitingTime(self, customers: List[List[int]]) -> float:
        start_order = 0
        waiting_time = []
        for arrive, time in customers:
            if arrive > start_order:
                start_order = arrive
            waiting_time.append((start_order + time) - arrive)
            start_order = start_order + time
        return sum(waiting_time) / len(customers)