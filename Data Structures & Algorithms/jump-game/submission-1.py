class Solution:
    def canJump(self, nums: List[int]) -> bool:
        maxR = 0
        for i in range(len(nums)):
            if i > maxR:
                return False
            maxR = max(maxR, i + nums[i])
        return True
        