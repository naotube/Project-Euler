def is_palindrome(string):
    """ if num is palindromic(:be read as same from both of right/left sides), return True

        >>> is_palindrome('123')
        False
        >>> is_palindrome('787')
        True
        >>> is_palindrome('9483')
        False
        >>> is_palindrome('5665')
        True
        >>> is_palindrome('56165')
        True
    """
    index = 0
    if string[0] == '0':
        return False
    while index < len(string) / 2:
        if not string[index] == string[-(index+1)]:
            return False
        index = index + 1
    return True

if __name__ == "__main__":
    import doctest
    doctest.testmod()

    LIMIT = 1000000
    palindromic_base2_base10 = []
    palindrome_numbers = [number for number in range(1,LIMIT) if is_palindrome(str(number))]
    for number in palindrome_numbers:
        if is_palindrome(bin(number)[2:]):
            palindromic_base2_base10.append(number)
    print(palindromic_base2_base10)
    print(sum(palindromic_base2_base10))
