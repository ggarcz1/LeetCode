class Solution(object):
    def moveZeroes(self, nums):
        """
        :type nums: List[int]
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        idx = 0
        for val in nums:
            if val != 0:
                # move number 
                nums[idx] = val
                idx += 1
                
        while idx < len(nums):
            nums[idx] = 0
            idx += 1
