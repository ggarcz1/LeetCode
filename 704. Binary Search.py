   def search(self, nums, target):
    """
    :type nums: List[int]
    :type target: int
    :rtype: int
    """
    head = 0
    tail = len(nums) - 1
    while head <= tail:
        mid = (head + (tail - head)/2)
        if nums[mid] > target:
            tail = mid - 1
        elif nums[mid] < target:
            head = mid + 1
        else:
            return mid

    return -1