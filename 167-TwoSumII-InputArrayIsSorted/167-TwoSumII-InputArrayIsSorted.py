# Last updated: 14/07/2026, 23:55:13
1class Solution(object):
2    def twoSum(self, numbers, target):
3        left=0
4        right=len(numbers)-1
5
6        while left<right:
7            if numbers[left]+numbers[right]<target:
8                left+=1
9            elif numbers[left]+numbers[right]>target:
10                right-=1
11            if numbers[left]+numbers[right]==target:
12                return [left+1,right+1]
13        