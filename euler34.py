if __name__ == "__main__":
    from math import factorial

    LIMIT = factorial(9)*7
    curious_numbers = []
    for number in range(3,LIMIT):
        sum_of_factorial = 0
        for digit in str(number):
            sum_of_factorial += factorial(int(digit))
        if sum_of_factorial == number:
            curious_numbers.append(number)
    print(curious_numbers)
    print(sum(curious_numbers))
