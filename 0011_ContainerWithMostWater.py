# 11. Container With Most Water

"""
Runtime: 128 ms, faster than 79.19% of Python3 online submissions for Container With Most Water.
Memory Usage: 14.4 MB, less than 81.05% of Python3 online submissions for Container With Most Water.
"""

class Solution:
    def maxArea(self, height: List[int]) -> int:
        # Two Pointer Approach
        length = len(height)
        if length < 2:
            return 0
        i = 0
        j = length - 1
        val = 0
        while i < j:
            tmp = min([height[i], height[j]]) * (j - i)
            if tmp > val:
                val = tmp
            if height[i] > height[j]:
                j -= 1
            else:
                i += 1
        return val
        
        # Brute Force (Time Limit Exceeded)
        """
        length = len(height)
        if length < 2:
            return 0
        val = 0
        for i in range(length - 1):
            for j in range(i+1, length):
                tmp = min([height[i], height[j]]) * (j - i)
                if tmp > val:
                    val = tmp
                    
        return val
        """
