def majorityElement(self, nums):
    """
    :type nums: List[int]
    :rtype: int
    """
    my_dict = {}
    val = nums[0]
    for idx in nums:
        if idx in my_dict:
            my_dict[idx] = my_dict[idx] + 1
        else:
            my_dict[idx] = 1
            
        # compare/set the max value here
        if my_dict[idx] > my_dict[val]:
            val = idx
    return val