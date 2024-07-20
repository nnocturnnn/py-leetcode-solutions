HEALTH = 1
DIRECTION = 2
ID = 3
TOP = -1

class Solution:
    def survivedRobotsHealths(self, positions: List[int], healths: List[int], directions: str) -> List[int]:
        robots = [[positions[ind], healths[ind], directions[ind], ind] for ind in range(len(positions))]
        robots.sort()
        stack = []

        for robot in robots:
            if robot[DIRECTION] == 'R':
                stack.append(robot)
            else:
                survive = True
                while stack and survive\
                    and stack[TOP][DIRECTION] == 'R':
                    if robot[HEALTH] > stack[TOP][HEALTH]:
                        robot[HEALTH] -= 1
                        stack.pop()
                    elif robot[HEALTH] < stack[TOP][HEALTH]:
                        stack[TOP][HEALTH] -= 1
                        survive = False
                    else:
                        stack.pop()
                        survive = False
                if survive:
                    stack.append(robot)
        stack.sort(key=lambda robot: robot[ID])
        return [robot[HEALTH] for robot in stack]

            