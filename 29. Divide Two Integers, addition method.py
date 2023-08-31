class Solution(object):
    def divide(self, dividend, divisor):
        """
        :type dividend: int
        :type divisor: int
        :rtype: int
        """
        if dividend == 0:
            return 0
        elif divisor == dividend:
            return 1
        elif divisor == 1:
            return dividend
        elif divisor == -1:
            return dividend * -1

        neg = False
        if divisor < 0 or dividend < 0:
            neg = True
        
        divisor = abs(divisor)
        dividend = abs(dividend)
        counter = 0 
        num = 0    
        while num <= dividend:
            num += divisor
            counter += 1
        if neg:
            return (counter - 1) * -1
        return counter - 1 
