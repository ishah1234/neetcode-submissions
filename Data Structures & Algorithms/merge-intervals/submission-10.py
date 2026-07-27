class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort()
        res = [intervals[0]] #1,3
        for start, end in intervals[1:]: 
            prevend = res[-1][1] #3
            if start <= prevend:
                res[-1][1] = max(prevend, end)
            else:
                res.append([start,end])
        return res