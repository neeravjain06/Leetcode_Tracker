# Last updated: 15/07/2026, 18:29:08
1class Solution(object):
2    def maxArea(self, height):
3        left = 0
4        right = len(height) - 1
5
6        maximum = 0
7
8        while left < right:
9
10            width = right - left
11            curr = width * min(height[left], height[right])
12
13            maximum = max(maximum, curr)
14
15            if height[left] < height[right]:
16                left += 1
17            else:
18                right -= 1
19
20        return maximum