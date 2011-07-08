import itertools

if __name__ == "__main__":
    primes = [2,3,5,7,11,13,17]
    digits = ['0','1','2','3','4','5','6','7','8','9']

    pandigital_numbers = itertools.permutations(digits)
    pandigital_numbers = ["".join(n) for n in pandigital_numbers if not n[0] == '0']
    interesting_numbers = [int(n) for n in pandigital_numbers if all(int(n[i+1:i+4]) % primes[i] == 0 for i in range(len(n) - 3))]
    print(sum(interesting_numbers))
