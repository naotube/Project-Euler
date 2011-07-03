def fifth_powers_number(number):
    """
    returns 1**5 + 2**5 + 3**5 + 4**5, for a number 1234.
    and like that.
    """
    numbers = str(number)
    sum_of_fifth_powers = 0
    for n in numbers:
        sum_of_fifth_powers = sum_of_fifth_powers + int(n) ** 5
    return sum_of_fifth_powers

if __name__ == "__main__":
    fifth_powers_numbers = []
    for i in range(2,(9**5)*6):
        if i == fifth_powers_number(i):
            fifth_powers_numbers.append(i)
    result = sum(fifth_powers_numbers)
    print(result)
