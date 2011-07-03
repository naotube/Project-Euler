import util_euler

if __name__ == "__main__":
    distinct_terms = []
    for a in range(2,101):
        prime_factors = util_euler.find_prime_factors(a)
        for b in range(2,101):
            term = []
            for x in range(b):
                term += prime_factors
            term.sort()
            if term not in distinct_terms:
                distinct_terms.append(term)

    print(len(distinct_terms))

