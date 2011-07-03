if __name__ == "__main__":
    fractional_part = ''
    number = 1
    while True:
        if len(fractional_part) > 1000000:
            break
        fractional_part = fractional_part + str(number)
        number += 1
    digits = []
    digits.append(int(fractional_part[1-1]))
    digits.append(int(fractional_part[10-1]))
    digits.append(int(fractional_part[100-1]))
    digits.append(int(fractional_part[1000-1]))
    digits.append(int(fractional_part[10000-1]))
    digits.append(int(fractional_part[100000-1]))
    digits.append(int(fractional_part[1000000-1]))
    result = 1
    for i in digits:
        result *= i
    print(result)

