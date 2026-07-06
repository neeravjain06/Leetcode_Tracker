# Last updated: 06/07/2026, 21:55:35
class Solution(object):
    def topKFrequent(self, nums, k):
        mp = {}

        # Count frequencies
        for num in nums:
            if num in mp:
                mp[num] += 1
            else:
                mp[num] = 1

        # Sort by frequency in descending order
        freq = sorted(mp.items(), key=lambda x: x[1], reverse=True)

        ans = []

        # Take first k elements
        for i in range(k):
            ans.append(freq[i][0])

        return ans