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
