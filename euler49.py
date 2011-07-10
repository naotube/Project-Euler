from itertools import combinations
import util_euler

def is_permutation(a, b):
    assert type(a).__name__ == 'int'
    assert type(b).__name__ == 'int'

    list_a = [c for c in str(a)]
    list_b = [c for c in str(b)]
    list_a.sort()
    list_b.sort()
    if list_a == list_b:
        return True
    return False

if __name__ == "__main__":
    primes = [i for i in util_euler.prime_generator(maximum=9999) if i > 999]
    unusual_sequence = [sequence for sequence in combinations(primes, 3)
                        if sequence[1] - sequence[0] == sequence[2] - sequence[1]
                        and is_permutation(sequence[0],sequence[1])
                        and is_permutation(sequence[1],sequence[2])
                        and not sequence[0] == 1487]
    answer = unusual_sequence[0]
    print(str(answer[0]) + str(answer[1]) + str(answer[2]))
