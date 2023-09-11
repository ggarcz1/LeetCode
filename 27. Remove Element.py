class Solution(object):
    def removeElement(self, nums, val):
        """
        :type nums: List[int]
        :type val: int
        :rtype: int
        """
        idx = 0
        # move all elements down if they != val
        for value in nums:
            if value != val:
                nums[idx] = value
                idx += 1
        # per directions, the first 'k' elements should be != val
        # therefore, idx serves as a counter
        return idx
