https://leetcode.com/problems/container-with-most-water/

class Solution:
    def maxArea(self, height: List[int]) -> int:
        i = 0 
        j = len(height)-1
        water = 0
        while(i<j):
            if height[i] < height[j] or height[i] == height[j]:
                line_height = height[i]
                width = j - i
                i += 1
                water = max(water,line_height * width)
            else:
                line_height = height[j]
                width = j - i
                j -= 1
                water = max(water,line_height * width)
        return water