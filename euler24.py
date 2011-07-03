TARGET = 1000000

from math import factorial

if __name__ == "__main__":
    number = TARGET - 1
    digits = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
    target_order = []
    while True:
        if len(digits) == 0:
            break
        count = 0
        while True:
            if number < factorial(len(digits) - 1):
                target_order.append(digits.pop(count))
                break
            number = number - factorial(len(digits) - 1)
            count = count + 1
    print(target_order)
