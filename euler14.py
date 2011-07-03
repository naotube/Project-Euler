def chain_len(number):
    """returns chain length
    >>> chain_len(13)
    10
    >>> chain_len(40)
    9
    >>> chain_len(20)
    8
    >>> chain_len(10)
    7
    """
    chain = 1
    while True:
        if number == 1:
            return chain
        if number % 2 == 0:
            number = number/2
        else:
            number = number * 3 + 1
        chain = chain + 1

if __name__=="__main__":
    import doctest
    doctest.testmod()

maximum = 0
number = 0
for i in range(1,1000001):
    chain = chain_len(i)
    if chain > maximum:
        maximum = chain
        number = i
        print(number)

print(number,maximum)
