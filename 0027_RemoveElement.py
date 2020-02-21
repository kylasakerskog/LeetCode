class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        nums_len = len(nums)
        i = 0
        if nums_len == 0:
            return 0;
        while i < nums_len:
            if nums[i] == val:
                nums.pop(i)
                nums_len -= 1
            else:
                i += 1
        return len(nums)
        
