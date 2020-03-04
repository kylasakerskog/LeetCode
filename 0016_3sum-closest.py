# 16. 3Sum Closest
"""
Runtime: 324 ms, faster than 21.50% of Python3 online submissions for 3Sum Closest.
Memory Usage: 12.8 MB, less than 100.00% of Python3 online submissions for 3Sum Closest.
"""
class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        if len(nums) < 3:
            return result
        nums.sort()
        result = nums[0] + nums[1] + nums[2] - target
        for i in range(0, len(nums)):
            s = i + 1
            e = len(nums) - 1

            if i > 0 and nums[i] == nums[i-1]:
                continue
            while s < e:
                dist = nums[i] + nums[s] + nums[e] - target
                print(i, s, e, result, dist)
                if dist < 0:
                    if abs(result) > (-1) * dist:
                        result = dist
                    s += 1
                elif dist > 0:
                    if abs(result) > dist:
                        result = dist
                    e -= 1
                else:
                    result = dist
                    return result + target
        return result + target
