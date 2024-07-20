class Solution:
    def minCost(self, colors: str, neededTime: List[int]) -> int:
        i = 0 
        ans = 0
        j = 0 
        while i < len(colors):
            max_time = neededTime[i]
            j = i
            while j < len(colors) and colors[j] == colors[i]:
                max_time = max(neededTime[j] , max_time)
                ans += neededTime[j]
                j += 1 
            ans -= max_time
            i = j 
        return ans 
