import util_euler

if __name__ == "__main__":
    import doctest
    doctest.testmod()

    LIMIT = 10000
    Lychrel_numbers = []

    for i in range(1,LIMIT):
        number = i
        count = 0
        while True:
            reverse_add_number = number + int(str(number)[::-1])
            count += 1
            if util_euler.is_palindrome(str(reverse_add_number)):
                break
            if count > 50:
                Lychrel_numbers.append(i)
                break
            number = reverse_add_number

    print("{0} Lychrel numbers exist below {1}".format(len(Lychrel_numbers), LIMIT))
