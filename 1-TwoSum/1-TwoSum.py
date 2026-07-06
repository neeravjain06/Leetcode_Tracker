# Last updated: 06/07/2026, 21:55:50
class Solution(object):
    def twoSum(self, nums, target):
        i=0
        mp={}
        
        for num in range(0,len(nums)):
            rem=target-nums[num]

            if rem in mp:
                return (mp[rem],num)
            mp[nums[num]]=num

            
        