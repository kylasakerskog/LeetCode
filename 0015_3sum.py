# 15. 3Sum
"""
Runtime: 1720 ms, faster than 22.54% of Python3 online submissions for 3Sum.
Memory Usage: 16.1 MB, less than 100.00% of Python3 online submissions for 3Sum.
"""
class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        result = set()
        if len(nums) < 3:
            return result
        nums.sort()
        for i in range(0, len(nums) - 2):
            s = i + 1
            e = len(nums) - 1
            while s < e:
                if (nums[i] + nums[s] + nums[e]) < 0:
                    s += 1
                elif (nums[i] + nums[s] + nums[e]) > 0:
                    e -= 1
                else: # nums[i] + nums[s] + nums[e] == 0
                    result.add((nums[i], nums[s], nums[e]))
                    while s < e and nums[s] == nums[s+1]:
                        s += 1
                    while s < e and nums[e] == nums[e-1]:
                        e -= 1
                    s += 1
                    e -= 1
        return result

class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        result = []
        if len(nums) < 3:
            return result
        nums.sort()
        for i in range(0, len(nums)):
            s = i + 1
            e = len(nums) - 1
            if i > 0 and nums[i] == nums[i-1]:
                continue
            while s < e:
                if (nums[i] + nums[s] + nums[e]) < 0:
                    s += 1
                elif (nums[i] + nums[s] + nums[e]) > 0:
                    e -= 1
                else: # nums[i] + nums[s] + nums[e] == 0
                    result.append([nums[i], nums[s], nums[e]])
                    s += 1
                    while s < e and nums[s] == nums[s-1]:
                        s = s + 1
        return result
