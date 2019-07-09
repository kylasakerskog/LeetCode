class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        l = len(nums)
        i = 0
        if(l == 0):
            return 0
        while i < l-1:
            if(nums[i] < nums[i+1]):
                i += 1
            else:
                nums.pop(i)
                l -= 1
        return len(list(nums))
