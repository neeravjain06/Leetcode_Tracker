# Last updated: 14/10/2026, 21:28:24
1class Solution(object):
2    def twoSum(self, numbers, target):
3        left=0
4        right=len(numbers)-1
5
6        while left<right:
7            if target-numbers[left]>numbers[right]:
8                left+=1
9            elif numbers[left]+numbers[right]==target:
10                return left+1,right+1
11            else:
12                right-=1
13            
14