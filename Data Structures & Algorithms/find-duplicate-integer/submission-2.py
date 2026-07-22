class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        # 1 2 3 2 2
        # 0 1 2 3 4
        slow, fast = nums[0], nums[0] # = 1
        while True:
            slow = nums[slow] # = 2
            fast = nums[nums[fast]] # 3
            if slow == fast:
                break
        
        slow2 = nums[0]
        while slow != slow2:
            slow = nums[slow]
            slow2 = nums[slow2]
        return slow