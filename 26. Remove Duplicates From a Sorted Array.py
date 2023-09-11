class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        length = len(nums)
        if length == 0 or length == 1:
            return length

        cmpValue = nums[0]
        counter = 0
        for idx in range(1, length):
            if nums[idx] == cmpValue:
                continue
            else:
                counter += 1
                cmpValue = nums[idx]
            nums[counter] = nums[idx]

        return counter+1