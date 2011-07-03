import util_euler

if __name__ == "__main__":
    LIMIT = 999
    A = 0
    B = 0
    MAX_N = 0
    for a in range(-LIMIT, LIMIT+1):
        for b in range(-LIMIT, LIMIT+1):
            n = 0
            consecutive_prime_count = 0
            while True:
                formula = n*n + a*n + b
                if not util_euler.is_prime(formula):
                    break
                consecutive_prime_count += 1
                n += 1
            if consecutive_prime_count > MAX_N:
                A, B, MAX_N = a, b, consecutive_prime_count
    print("a:{0} b:{1} max_n:{2}".format(A, B, MAX_N))
    print("answer:{0}".format(A*B))
