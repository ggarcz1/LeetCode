class Solution(object):
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        number = 0
        for idx in nums:
            number = number ^ idx
        return number 