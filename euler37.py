import util_euler

if __name__ == "__main__":
    truncatable_primes = []
    number = 10
    while True:
        number += 1
        if all(util_euler.is_prime(int(str(number)[i:])) for i in range(len(str(number)))):
            if all(util_euler.is_prime(int(str(number)[:-i])) for i in range(1,len(str(number)))):
                truncatable_primes.append(number)
                print(truncatable_primes)
        if len(truncatable_primes) == 11:
            break
    print("sum of truncatable primes is {0}".format(sum(truncatable_primes)))
