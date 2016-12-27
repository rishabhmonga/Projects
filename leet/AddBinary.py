def addBinary(a, b):
    """
    :type a: str
    :type b: str
    :rtype: str
    """
    if len(a) == 0: return b
    if len(b) == 0: return a
    if a[-1] == '1' and b[-1] == '1':
        return addBinary(addBinary(a[0:-1], b[0:-1]), '1') + '0'
    if a[-1] == '0' and b[-1] == '0':
        return addBinary(a[0:-1], b[0:-1]) + '0'
    else:
        return addBinary(a[0:-1], b[0:-1]) + '1'


if __name__ == '__main__':
    print(addBinary('11', '1'))
