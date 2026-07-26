class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        res = []
        def backtrack(i, curr, remaining): #2,5,6,9 t = 9
            if remaining == 0:
                res.append(curr.copy())
                return
            if remaining < 0 or i >= len(nums):
                return 
            curr.append(nums[i])
            backtrack(i, curr, remaining-nums[i])

            curr.pop()
            backtrack(i+1, curr, remaining)
        backtrack(0, [], target)
        return res

        