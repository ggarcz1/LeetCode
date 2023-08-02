class Solution(object):
    def alternateDigitSum(self, n):
        """
        :type n: int
        :rtype: int
        """
        sum = counter = 0
        # reverse number for case of power of 10 but even length
        n = int(str(n)[::-1])
        while n > 0:
            # mod  gets the value to add
            value = int(n % 10)
            # zero is neither pos or neg
            if value == 0:
                sum == sum
            # counter is even
            elif counter % 2 == 0:
                sum = sum + value
            # counter is odd
            elif counter % 2 == 1:
                sum = sum - value
            # divide pops off the remainder
            n = n / 10
            counter += 1
        return sum