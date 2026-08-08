class Solution:
    def maxOperations(self, nums: List[int], k: int) -> int:
        nums.sort()
        l = 0
        n = len(nums)
        r = n-1
        count = 0
        while l < r:
            summ = nums[l] + nums[r]
            if summ == k:
                count += 1
                l += 1
                r -= 1
            elif summ < k:
                l += 1
            elif summ > k:
                r -= 1
        return count
                

        