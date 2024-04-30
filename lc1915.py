from collections import defaultdict
"""
First notice that we only care about the parity of a 
letter, so it suffices to work in 0 and 1. 

The most important observation is that
each substring can be represented by the difference 
of two prefixes. Also note that if two prefix has 
the same bit mask, then every letter in their difference
occurs even # of times; and if their bit mask differs by 1
then exactly 1 of the letters (at which their mask differs)
occurs odd number of times.  
"""
class Solution:
    def wonderfulSubstrings(self, word: str) -> int:
        freq = defaultdict(lambda: 0)
        res = 0
        mask = 0
        freq[0] = 1
        for c in word:
            bit = ord(c) - ord("a")
            mask = mask ^ (1 << bit)
            res += freq[mask]
            freq[mask] += 1

            for x in range(10):
                res += freq[mask ^ (1 << x)]
        return res
