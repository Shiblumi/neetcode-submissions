class Solution:
    def maxArea(self, heights: List[int]) -> int:
        max_water = 0
        
        for i in range(len(heights)):
            r = len(heights) - 1
            while i < r:
                min_height = min(heights[i], heights[r])
                water = min_height * (r-i)
                max_water = max(max_water, water)
                r -= 1
        return max_water

        