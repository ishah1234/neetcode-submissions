class Solution:
    def jump(self, nums: List[int]) -> int:
        jumps, end, maxD = 0,0,0
        for i in range(len(nums)- 1):
            maxD = max(maxD, i+nums[i])

            if i == end:
                jumps += 1
                end = maxD
        return jumps