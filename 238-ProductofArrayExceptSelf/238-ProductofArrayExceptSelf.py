# Last updated: 07/07/2026, 23:30:49
1class Solution(object):
2    def productExceptSelf(self, nums):
3        left=1
4        right=1
5        ans=[1]*len(nums)
6        for i in range(len(nums)):
7            ans[i]*=left
8            left*=nums[i]
9        for i in range(len(nums)-1,-1,-1):
10            ans[i]*=right
11            right*=nums[i]
12        return ans
13        
14        
15
16        