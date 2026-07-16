# Last updated: 16/07/2026, 23:03:25
1class Solution(object):
2    def trap(self, height):
3        if not height:
4            return 0
5
6        left = 0
7        right = len(height) - 1
8
9        leftMax = height[left]
10        rightMax = height[right]
11
12        water = 0
13
14        while left < right:
15
16            if leftMax < rightMax:
17
18                left += 1
19
20                leftMax = max(leftMax, height[left])
21
22                water += leftMax - height[left]
23
24            else:
25
26                right -= 1
27
28                rightMax = max(rightMax, height[right])
29
30                water += rightMax - height[right]
31
32        return water