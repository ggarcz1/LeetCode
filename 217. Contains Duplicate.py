def containsDuplicate(self, nums):
    """
    :type nums: List[int]
    :rtype: bool
    """
    my_dict = {}
    for idx in nums:
        try:
            if my_dict[idx] == 1:
                return True
        except KeyError:
            my_dict[idx] = 1

    return False