class Solution:
    def search(self, nums: list[int], target: int) -> bool:
        l = 0
        r = len(nums) - 1
        while l <= r:
            mid = l + ((r-l)//2)
            if target == nums[mid] : return True
            elif nums[l] == nums[mid] and nums[r] == nums[mid]: 
                l += 1
                r -= 1
            elif nums[mid] <= nums[r]:
                if target > nums[mid] and target <= nums[r]: 
                    l = mid + 1
                else:
                    r = mid - 1
            else:
                if target >= nums[l] and target < nums[mid]: 
                    r = mid - 1
                else:
                    l = mid + 1
        return False
