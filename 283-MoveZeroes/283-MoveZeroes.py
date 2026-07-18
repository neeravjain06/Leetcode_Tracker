# Last updated: 18/07/2026, 16:49:05
1class Solution(object):
2    def moveZeroes(self, nums):
3        slow=0
4        fast=0
5
6        while fast!=len(nums):
7            if nums[fast]==0:
8                fast+=1
9                continue
10            else:
11                temp=nums[slow]
12                nums[slow]=nums[fast]
13                nums[fast]=temp
14                slow+=1
15                fast+=1
16                
17
18        return nums        