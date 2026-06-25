class Solution:
    def twoSum(self, nums:List[int], target: int) -> List[int]:
        set = {}
        for i, n in  enumerate(nums):
            set[n] = i
        for i, n in enumerate(nums):
            diff = target - n
            if diff in set and set[diff] != i:
                return [i, set[diff]]
        return []