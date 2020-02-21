class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        seen = {}
        for index, num in enumerate(nums):
            n =  target - num
            if n not in seen:
                seen[num] = index
            else:
                return [seen[n], index]
