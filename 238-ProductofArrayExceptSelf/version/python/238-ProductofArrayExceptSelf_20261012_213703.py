# Last updated: 12/10/2026, 21:37:03
1class Solution(object):
2    def productExceptSelf(self, nums):
3        ans=[1]*len(nums)
4        prefix=1
5
6        for i in range(len(nums)):
7            ans[i]=prefix
8            prefix*=nums[i]
9        suffix=1
10        for i in range(len(nums)-1,-1,-1): 
11            ans[i]*=suffix
12            suffix*=nums[i]       
13        return ans 
14        
15        
16        
17        
18        
19
20
21
22
23        
24        
25
26        