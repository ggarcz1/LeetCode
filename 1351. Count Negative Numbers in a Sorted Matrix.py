def countNegatives(self, grid):
    """
    :type grid: List[List[int]]
    :rtype: int
    """
    negativeCount = 0

    # since it is sorted in decreasing order
    # begin at end of each array and count backwards
    # if arr[end_Value] < 0
    # move on
    # else
    # negativeCount++

    negativeCount = 0
    for x in range(0, len(grid)):
        for j in range(len(grid[x])-1, -1, -1):
            if grid[x][j] < 0:
                negativeCount += 1

    return negativeCount 