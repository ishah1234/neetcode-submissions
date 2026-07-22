class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        hashmap = set()
        for n in nums:
            if n in hashmap:
                return n
            hashmap.add(n)