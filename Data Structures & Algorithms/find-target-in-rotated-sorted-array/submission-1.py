class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l , r = 0, len(nums)-1 # [3,4,5,6,7,1,2] nums[l]= 3, nums[r]=2, t= 4 or t=7, nums[m]=6

        while l <= r:
            m = (l+r) // 2
            if target == nums[m]:
                return m
            
            if nums[l] <= nums[m]:
                if nums[l]> target or nums[m]<target  :
                    l = m + 1
                else:
                    r = m - 1 
            else:
                if target > nums[r] or target < nums[m]:
                    r = m - 1
                else:
                    l = m + 1
        return -1
