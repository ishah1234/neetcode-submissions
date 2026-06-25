class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        set = {}
        for i, n in enumerate(nums):
            set[n] = i
        for i, n in enumerate(nums):
            difference = target - n
            if difference in set and set[difference] != i:
                return [i, set[difference]]
            
        return []