# Last updated: 06/07/2026, 21:55:32
class Solution(object):
    def isAnagram(self, s, t):
        freq={}

        if len(s)!=len(t):
            return False
        
        for ch in s:
            freq[ch]=freq.get(ch,0)+1
        for ch in t:
            freq[ch]=freq.get(ch,0)-1

        for val in freq.values():
            if val!=0:
                return False
        
        return True