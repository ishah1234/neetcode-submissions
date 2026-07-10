class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        lastIndex = {}
        for i, c in enumerate(s):
            lastIndex[c] = i

        last_occ = {}
        for i, c in enumerate(s):
            last_occ[c] = i
        res = []
        start,end = 0,0
        for i,c in enumerate(s):
            end = max(end, last_occ[c])
            if i == end:
                res.append(end-start+1)
                start = i + 1 

        return res