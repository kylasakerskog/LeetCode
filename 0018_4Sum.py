# 18. 4Sum
"""
Runtime: 1516 ms, faster than 14.56% of Python3 online submissions for 4Sum.
Memory Usage: 12.7 MB, less than 100.00% of Python3 online submissions for 4Sum.
"""

class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        result = set()
        if len(nums) < 4:
            return result
        nums.sort()
        for i in range(0, len(nums) - 3):
            for j in range(i + 1, len(nums) - 2):
                s = j + 1
                e = len(nums) - 1
                while s < e:
                    if (nums[i] + nums[j] + nums[s] + nums[e]) < target:
                        s += 1
                    elif (nums[i] + nums[j] + nums[s] + nums[e]) > target:
                        e -= 1
                    else: # nums[j] + nums[i] + nums[s] + nums[e] == 0
                        result.add((nums[i], nums[j], nums[s], nums[e]))
                        while s < e and nums[s] == nums[s+1]:
                            s += 1
                        while s < e and nums[e] == nums[e-1]:
                            e -= 1
                        s += 1
                        e -= 1
        return result
