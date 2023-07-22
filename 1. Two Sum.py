def twoSum(self, nums, target):
    """
    :type nums: List[int]
    :type target: int
    :rtype: List[int]
    """
    if len(nums) == 0:
        return []
    arr = []
    for idx in range(0, len(nums)-1):
        for val in range(idx+1,len(nums)-1):
             if nums[idx]+nums[val] == target:
                arr.append(idx)
                arr.append(val)

    return arr