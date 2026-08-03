class Solution:
    def maxArea(self, height: List[int]) -> int:
        l, r = 0, len(height)-1
        maxnum = 0
        while l<r:
            hl, hr = height[l], height[r]
            if hl > hr:
                cur = hr*(r-l)
                maxnum = max(cur, maxnum)
                while l<r and height[r]<=hr:
                    r-=1
            else:
                cur = hl*(r-l)
                maxnum = max(cur, maxnum)
                while l<r and height[l]<=hl:
                    l+=1
        return maxnum