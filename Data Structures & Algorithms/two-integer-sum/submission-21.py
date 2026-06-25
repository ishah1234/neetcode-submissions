class Solution:
    def twoSum(self, nums:List[int], target: int) -> List[int]:
        map = {}
        for i, n in enumerate(nums):
            map[n] = i
        for i, n in enumerate(nums):
            difference = target - n
            if difference in map and map[difference] != i:
                return [i, map[difference]] 
        return []          