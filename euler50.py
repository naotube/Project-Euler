import util_euler
import itertools

if __name__ == "__main__":
    MAXIMUM = 1000000
    gen = util_euler.prime_generator(MAXIMUM)
    primes = [i for i in gen]
    sums_of_consecutive_primes = []
    sum_of_primes = 0
    for i in primes:
        sum_of_primes += i
        if sum_of_primes > MAXIMUM:
            break
        sums_of_consecutive_primes.append(sum_of_primes)
    sums_of_consecutive_primes = itertools.combinations(sums_of_consecutive_primes, 2)
    sums_of_consecutive_primes = set([i[1] - i[0] for i in sums_of_consecutive_primes])
    for i in primes[::-1]:
        if i in sums_of_consecutive_primes:
            answer = i
            break
    print(answer)
