class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        candidates.sort()
        res = []
        def backtrack(i, curr, remaining):
            if remaining == 0:
                res.append(curr.copy())
                return 
            if remaining < 0 or i >= len(candidates):
                return 
            
            for j in range(i, len(candidates)):
                if j > i and candidates[j] == candidates[j-1]:
                    continue
                
                curr.append(candidates[j])
                backtrack(j+1, curr, remaining-candidates[j])
                curr.pop()
        backtrack(0,[], target)
        return res