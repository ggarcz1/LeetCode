class Solution(object):
    def addBinary(self, a, b):
        """
        :type a: str
        :type b: str
        :rtype: str
        """
        if a == "0" and b == "0":
            return "0"
        total = int(a, 2) + int(b, 2)
        rtVal = ''

        while total > 0:
            rtVal += str(total % 2)
            total = total / 2

        rtVal = rtVal[::-1]

        return rtVal