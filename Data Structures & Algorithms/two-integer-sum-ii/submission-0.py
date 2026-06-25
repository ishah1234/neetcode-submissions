class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        map = defaultdict(int)
        for i in range(len(numbers)):
            target_map = target - numbers[i]
            if map[target_map]:
                return [map[target_map], i + 1]
            map[numbers[i]] = i + 1
        return []