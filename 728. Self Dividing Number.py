class Solution:
    def selfDividingNumbers(self, left: int, right: int) -> List[int]:
        """
        :type left: int
        :type right: int
        :rtype: List[int]
        """
        lst = []
        for idx in range(left, right+1):
            value = idx
            torf = True
            arr = [*str(idx)]
            for value in arr:
                if int(value) == 0: 
                    torf = False
                    break
                elif idx % int(value) == 0:
                    continue
                else:
                    torf = False
                    break
            if torf:
                lst.append(idx)

        return lst    