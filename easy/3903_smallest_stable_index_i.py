class Solution:
    def firstStableIndex(self, nums: list[int], k: int) -> int:
        n = len(nums)
        l = 0
        r = n - 1
        minn = [0] * n
        maxx = [0] * n
        maxxl, minnr = nums[0], nums[-1]
        while l < n:
            currl = nums[l]
            currr = nums[r]
            if currl > maxxl: maxxl = currl
            if currr < minnr: minnr = currr
            maxx[l] = maxxl
            minn[r] = minnr
            l += 1
            r -= 1
        for i in range(n):
            if maxx[i]-minn[i] <= k: return i
        return -1  