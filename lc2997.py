class Solution(object):
    """
    Consider XOR as summation in Z2. It doesn't really matter
    which element we apply bitflip on. As long as they are in the 
    right locations. 
    To determine the locations, just XOR all original elmenets and 
    compare the result with k. 
    """
    def minOperations(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        n = 0
        for num in nums:
            n ^= num
        return bin(n ^ k).count('1')
        
