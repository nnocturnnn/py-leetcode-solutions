from datetime import datetime

class Solution:
    def countDaysTogether(self, arriveAlice: str, leaveAlice: str, arriveBob: str, leaveBob: str) -> int:
        arrive_alice_date = datetime.strptime(arriveAlice, "%m-%d")
        leave_alice_date = datetime.strptime(leaveAlice, "%m-%d")
        arrive_bob_date = datetime.strptime(arriveBob, "%m-%d")
        leave_bob_date = datetime.strptime(leaveBob, "%m-%d")
        
        start_date = max(arrive_alice_date, arrive_bob_date)
        end_date = min(leave_alice_date, leave_bob_date)

        if start_date <= end_date: 
            days_together = (end_date - start_date).days + 1
        else:
            days_together = 0

        return days_together
