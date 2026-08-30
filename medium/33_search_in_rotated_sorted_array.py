class Solution:
    def search(self, nums: List[int], target: int) -> int:
        n = len(nums)
        l = 0
        r = n - 1
        while l <= r:
            m = l + ((r-l)// 2)
            if nums[m] == target: return m
            elif nums[r] > nums[m] : 
                if target > nums[m] and target <= nums[r]:
                    l = m  + 1
                else:
                    r = m - 1
            else: 
                if target < nums[m] and target >= nums[l]:
                    r = m - 1
                else:
                    l = m + 1
        return -1
            
                