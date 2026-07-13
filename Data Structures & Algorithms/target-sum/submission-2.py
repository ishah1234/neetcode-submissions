class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        dp = {0 : 1}
        for n in nums:
            newDp = {}
            for curSum, count in dp.items():
                newDp[curSum + n] = newDp.get(curSum + n, 0) + count
                newDp[curSum - n] = newDp.get(curSum - n, 0) + count
            dp = newDp
        return dp.get(target, 0)