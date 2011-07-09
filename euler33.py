def curious_cancell(numerator, denominator):
    """cancell a digit in both of numerator and denominator
    >>> curious_cancell(49, 98)
    (4, 8)
    """
    if str(numerator)[0] == str(denominator)[0]:
        return (int(str(numerator)[1]), int(str(denominator)[1]))
    elif str(numerator)[0] == str(denominator)[1]:
        return (int(str(numerator)[1]), int(str(denominator)[0]))
    elif str(numerator)[1] == str(denominator)[0]:
        return (int(str(numerator)[0]), int(str(denominator)[1]))
    elif str(numerator)[1] == str(denominator)[1]:
        return (int(str(numerator)[0]), int(str(denominator)[0]))
    else:
        return None

if __name__ == "__main__":
    import util_euler

    curious_fractions = []
    fractions = [(n, d) for n in range(11,100) for d in range(11,100) if n < d \
                and len(set(str(n) + str(d))) < 4 \
                and not (n % 10 == 0 and d % 10 == 0) \
                and (str(n)[0] in str(d) or str(n)[1] in str(d))]
    for f in fractions:
        numerator = f[0]
        denominator = f[1]
        curious_cancelled = curious_cancell(numerator, denominator)
        if not curious_cancelled[1] == 0 and curious_cancelled[0] / curious_cancelled[1] == numerator / denominator:
            curious_fractions.append((numerator,denominator))

    prime_factors_of_numerator = []
    product_of_denominators = 1
    for c in curious_fractions:
        prime_factors_of_numerator += util_euler.find_prime_factors(c[0])
        product_of_denominators *= c[1]
    for i in prime_factors_of_numerator:
        if product_of_denominators % i == 0:
            product_of_denominators /= i
    print("answer: {0}".format(int(product_of_denominators)))
