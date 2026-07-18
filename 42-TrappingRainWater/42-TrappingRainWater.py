# Last updated: 18/07/2026, 15:15:47
1class Solution(object):
2    def trap(self, height):
3        left=0
4        right=len(height)-1
5
6        leftMax=height[left]
7        rightMax=height[right]
8
9        water=0
10
11        while left<right:
12
13            if leftMax<rightMax:
14                left+=1
15                leftMax=max(leftMax,height[left])
16                water+=leftMax-height[left]
17            else:
18                right-=1
19                rightMax=max(rightMax,height[right])
20                water+=rightMax-height[right]
21        return water 
22