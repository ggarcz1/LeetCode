def lengthOfLastWord(self, s):
    """
    :type s: str
    :rtype: int
    """
    s = s.strip()
    val = s.split(' ')
    return len(val[len(val)-1])