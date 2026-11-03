class Solution:
    def maxArea(self, height: list[int]) -> int:
        l, r = 0, len(height) - 1
        max_area = 0
        while l < r:
            tall = min(height[l], height[r])
            width = r - l

            if width * tall > max_area:
                max_area = width * tall
            
            if height[l] < height[r]:
                l += 1
            else:
                r -= 1
        return max_area
