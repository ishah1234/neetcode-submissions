class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        i = 0 
        n = len(intervals)
        res = []

        while i < n and intervals[i][1] < newInterval[0]:     #[1,2] curr and [6,7]new  loop for before 
            res.append(intervals[i])
            i += 1
        while i < n and intervals[i][0] <= newInterval[1]:   # [1,3]curr and [2,5]new overlap
            newInterval[0] = min(newInterval[0], intervals[i][0])
            newInterval[1] = max(newInterval[1], intervals[i][1])
            i += 1
        res.append(newInterval)
        while i < n:   #[6,7] new and [9,10] curr 
            res.append(intervals[i])
            i += 1
        return res