import util_euler
from itertools import combinations

def is_brother(a, b):
    """
    >>> is_brother(123, 223)
    True
    >>> is_brother(463, 683)
    False
    >>> is_brother(739, 769)
    True
    >>> is_brother(739, 739)
    True
    """
    if a == b:
        return True
    a, b = str(a), str(b)
    if not len(a) == len(b):
        return False
    differences = [int(b[i]) - int(a[i]) for i in range(len(a))]
    if not len(set(differences)) == 2:
        return False
    if not 0 in differences:
        return False
    if not len([int(a[i]) * differences[i] for i in range(len(a)) if not differences[i] == 0]) == 1:
        return False
    return True

def are_brothers(a, b):
    """
    >>> are_brothers((337, 367, 397), (307, 337))
    True
    >>> are_brothers((491, 499), (491, 691))
    False
    """
    from itertools import product
    pairs = product(a, b)
    if all(is_brother(pair[0], pair[1]) for pair in pairs):
        return True
    return False

if __name__ == "__main__":
    import doctest
    doctest.testmod()
    maximum = 10
    answer = 0

    while maximum < 10000:
        gen = util_euler.prime_generator(maximum)
        prime_brother = [p for p in combinations(gen,2) if is_brother(p[0], p[1])]

        tuple_length = 2
        while len(prime_brother) > 0:
            prime_brother = list(set([tuple(set(p[0] + p[1])) for p in combinations(prime_brother, 2) if are_brothers(p[0], p[1])]))
            prime_brother = [p for p in prime_brother if len(p) > tuple_length]
            print(prime_brother)
            # conditional statement for break may not be correct
            if tuple_length == 6 and len(prime_brother) > 0:
                answer = min(prime_brother[0])
            tuple_length += 1
        if not answer == 0:
            break
        maximum *= 10

    print("answer: {0}".format(answer))
