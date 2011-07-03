# A palindromic number reads the same both ways.
# The largest palindrome made from the product of two 2-digit numbers is 9009 = 91 × 99.
# Find the largest palindrome made from the product of two 3-digit numbers.

def is_palindrome(num):
    """ if num is palindromic(:be read as same from both of right/left sides), return True

        >>> is_palindrome(123)
        False
        >>> is_palindrome(787)
        True
        >>> is_palindrome(9483)
        False
        >>> is_palindrome(5665)
        True
    """
    index = 0
    while index < len(str(num)):
        if not str(num)[index] == str(num)[-(index+1)]:
            return False
        index = index + 1
    return True

if __name__ == "__main__":
    import doctest
    doctest.testmod()

    maximum = 0
    for i in range(100,1000):
        for j in range(100,1000):
            if is_palindrome(i*j):
                if i*j > maximum:
                    maximum = i*j
    print(maximum)
