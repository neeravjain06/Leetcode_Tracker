# Last updated: 08/09/2026, 09:24:34
1class Solution(object):
2    def twoSum(self, nums, target):
3        i=0
4        mp={}
5        
6        for num in range(0,len(nums)):
7            rem=target-nums[num]
8
9            if rem in mp:
10                return (mp[rem],num)
11            mp[nums[num]]=num
12
13            
14        