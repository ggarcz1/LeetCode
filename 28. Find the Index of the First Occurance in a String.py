class Solution(object):
    def strStr(self, haystack, needle):
        """
        :type haystack: str
        :type needle: str
        :rtype: int
        """
        # edge cases
        if len(haystack) < len(needle):
            return -1
        if haystack == needle:
            return 0
        
        # check if it exists in the haystack
        for pos in range(0,len(haystack)-len(needle)+1):
            if haystack[pos] == needle[0]:
                if haystack[pos:(pos+len(needle))] == needle:
                    return pos
        return -1
        
        