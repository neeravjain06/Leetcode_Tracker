# Last updated: 06/07/2026, 22:47:47
1class Solution(object):
2    def topKFrequent(self, nums, k):
3        freq = defaultdict(int)
4
5        # Count frequencies
6        for num in nums:
7            freq[num] += 1
8
9        # Create buckets
10        bucket = [[] for _ in range(len(nums) + 1)]
11
12        # Place numbers into buckets
13        for num, count in freq.items():
14            bucket[count].append(num)
15
16        ans = []
17
18        # Traverse buckets from highest frequency to lowest
19        for i in range(len(bucket) - 1, 0, -1):
20            for num in bucket[i]:
21                ans.append(num)
22
23                if len(ans) == k:
24                    return ans
25
26        