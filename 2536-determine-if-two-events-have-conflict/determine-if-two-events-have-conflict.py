from datetime import datetime

class Solution:
    def haveConflict(self, event1: List[str], event2: List[str]) -> bool:
        return not (datetime.strptime(event1[1], "%H:%M") < datetime.strptime(event2[0], "%H:%M") or datetime.strptime(event2[1], "%H:%M") < datetime.strptime(event1[0], "%H:%M"))