class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        res = []

        def backtrack(curr, remaining):
            if not remaining:
                res.append(curr.copy())
                return

            for i in range(len(remaining)):
                curr.append(remaining[i])
                backtrack(curr, remaining[:i] + remaining[i+1:])
                curr.pop()

        backtrack([], nums)
        return res
            