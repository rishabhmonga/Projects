def isPalindrome(s):
    """
    :type s: str
    :rtype: bool
    """
    l, r = 0, len(s) - 1
    while l < r:
        while l < r and not s[l].isalnum():
            l += 1
        while l < r and not s[r].isalnum():
            r -= 1
        if s[l].lower() != s[r].lower():
            return False
        l += 1
        r -= 1
    return True


def palindrome(s):
    l, r = 0, len(s) - 1
    while l < r:
        if s[l] != s[r]:
            return False
        l += 1
        r -= 1
    return True


if __name__ == '__main__':
    # print(isPalindrome("A man, a plan, a canal: Panama"))
    # print(isPalindrome("aa"))
    # print(isPalindrome("race a car"))

    print(palindrome('aa'))
    print(palindrome('b'))