from itertools import count
import util_euler

if __name__ == "__main__":
    CONSECUTIVE = 4
    prime_factor_lists = []

    for i in count(1):
        prime_factor_lists.append(util_euler.find_prime_factors(i))
        if len(prime_factor_lists) > CONSECUTIVE:
            prime_factor_lists.remove(prime_factor_lists[0])
        if all(len(set(prime_factors)) == CONSECUTIVE for prime_factors in prime_factor_lists):
            answer = i - (CONSECUTIVE - 1)
            break
    print("answer: {0}".format(answer))

