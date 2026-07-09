# Last updated: 09/07/2026, 22:25:10
1class Solution(object):
2    def longestConsecutive(self, nums):
3        numSet=set(nums)
4        length=0
5        for num in numSet:
6            
7            if num-1 not in numSet:
8                longest=1
9                while num+longest in numSet:
10                    longest+=1
11                length=max(longest,length)
12        return length
13                
14        
15        