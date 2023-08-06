def accountBalanceAfterPurchase(self, purchaseAmount):
    """
    :type purchaseAmount: int
    :rtype: int
    """
    if purchaseAmount <= 0:
        return 100
    rounded = 0
    actual = 100 - purchaseAmount
    if actual % 10 > 5:
        rounded = actual + 10 - (actual % 10)
    else:
        rounded = actual - (actual % 10)
    return rounded