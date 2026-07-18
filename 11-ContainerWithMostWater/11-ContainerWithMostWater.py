# Last updated: 18/07/2026, 14:34:41
1class Solution(object):
2    def maxArea(self, height):
3        left=0
4        right=len(height)-1
5
6        max=0
7
8        while left<right:
9            curr=(right-left)*min(height[left],height[right])
10
11            if max<curr:
12                max=curr
13            
14            if height[left]<height[right]:
15                left+=1
16            else:
17                right-=1
18        return max
19
20