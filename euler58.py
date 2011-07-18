import util_euler

if __name__ == "__main__":
    count = 0
    numbers_on_diagonal = 1
    primes_on_diagonal = 0
    number = 1
    layer = 1
    while True:
        number += 2 * layer
        count += 1
        if util_euler.is_prime(number):
            primes_on_diagonal += 1
        numbers_on_diagonal += 1
        if count % 4 == 0:
            if primes_on_diagonal / numbers_on_diagonal < 0.1:
                side_length = 2 * layer + 1
                break
            count = 0
            layer += 1
    print("answer: {0}".format(side_length))
