class Solution(object):
    def maximumCount(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        # count forward and when - switch to +
        # could also say if negative_count > len(arr)/2, return negative_count
        # return max(current_index, rest_of_array)
        pos = 0
        neg = 0
        for idx in range(0, len(nums)):
            if nums[idx] > 0:
                pos += 1
            elif nums[idx] < 0:
                neg += 1
        return max(pos, neg)