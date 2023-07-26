def toLowerCase(self, s):
    """
    :type s: str
    :rtype: str
    """
    for idx in range(0, len(s)):
        value = ord(s[idx])
        # if ascii is upper case
        if value <= 90 and value >= 65:
            s = s.replace(chr(value), chr(value+32))

    return s