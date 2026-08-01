class Solution:
    def maxArea(self, height):
        n = len(height)
        r = n-1
        l = 0
        max_height = 0
        while l < r:
            max_height = max(max_height,min(height[l], height[r]) * (r-l))
            if height[l] >= height[r]:
                r -= 1
            else:
                l += 1
        return max_height

        