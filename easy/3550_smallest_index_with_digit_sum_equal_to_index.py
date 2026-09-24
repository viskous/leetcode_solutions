class Solution:
    def smallestIndex(self, nums: List[int]) -> int:
        summ = 0
        for i in range(len(nums)):
            n = nums[i]
            while n > 0:
                summ += n%10
                n = n//10
            if summ == i:
                return i
            summ = 0
        return -1