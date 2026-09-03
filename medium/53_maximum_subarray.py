class Solution:
    def maxSubArray(self, nums):
        curr_sum = 0
        max_sum = -(10**4)
        for r in nums:
            curr_sum += r
            if curr_sum > max_sum:
                max_sum = curr_sum
            if curr_sum < 0:
                curr_sum = 0
        return max_sum