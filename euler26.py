if __name__ == "__main__":
    LIMIT = 1000
    number = 0
    longest_cycle = 0

    for i in range(1,LIMIT):
        dividend = 1
        quotients_and_remainders = []
        while True:
            quotient = dividend // i
            if quotient == 0:
                quotients_and_remainders.append([quotient, dividend])
                dividend *= 10
            else:
                remainder = dividend % i
                if remainder == 0:
                    break
                if quotients_and_remainders.count([quotient, remainder]) > 0:
                    cycle = len(quotients_and_remainders[quotients_and_remainders.index([quotient, remainder]):])
                    if cycle > longest_cycle:
                        longest_cycle = cycle
                        longest_cycle_number = i
                    break
                quotients_and_remainders.append([quotient, remainder])
                dividend = remainder * 10
    print("the longest cycle number is {0}".format(longest_cycle_number))
