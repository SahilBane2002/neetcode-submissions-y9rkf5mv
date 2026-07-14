class Solution:
    def maxArea(self, heights: List[int]) -> int:
        volume = 0
        d = 0
        left = 0
        right = len(heights) - 1

        while left < right:
            newVolume = (right - left) * min(heights[left], heights[right])
            if heights[left] > heights[right]:
                right -= 1
            elif heights[left] < heights[right]:
                left += 1
            else:
                right -= 1
                left += 1
            volume = max(volume, newVolume)

        return volume



