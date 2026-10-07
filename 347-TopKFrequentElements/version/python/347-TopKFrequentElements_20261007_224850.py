# Last updated: 07/10/2026, 22:48:50
1class Solution(object):
2    def topKFrequent(self, nums, k):
3        freq = defaultdict(int)
4
5        for i in nums:
6            freq[i] += 1
7
8# Sort the elements by their frequency
9        sorted_nums = sorted(freq, key=freq.get, reverse=True)
10
11        ans = []
12
13        for i in range(k):
14            ans.append(sorted_nums[i])
15
16        return ans
17        
18
19        