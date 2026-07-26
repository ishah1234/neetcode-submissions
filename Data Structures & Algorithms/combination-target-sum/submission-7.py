class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        res = []
        def backt(i, curr, remaining):
            if remaining == 0:
                res.append(curr.copy())
                return 
            if i >= len(nums) or remaining < 0:
                return
            curr.append(nums[i])
            backt(i, curr, remaining-nums[i])

            curr.pop()
            backt(i+1, curr, remaining)

        backt(0, [], target)
        return res

        