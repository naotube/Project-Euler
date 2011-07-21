import util_euler

LIMIT = 1000000

#maximum_n_phi = 0
#for n in range(1, LIMIT + 1):
#    prime_factors = set(util_euler.find_prime_factors(n))
#    relatively_prime = len([p for p in range(1, n + 1) if all(not p % q == 0 for q in prime_factors)])
#    n_phi = n / relatively_prime
#    if n_phi > maximum_n_phi:
#        maximum_n_phi = n_phi
#        answer = n
#        print(n)
#

# the code above indicates that the answer is the product of primes.
# 2, 6, 30, 210, 2310, 30030
# so...

gen = util_euler.prime_generator()
answer = 1
for i in gen:
    answer *= i
    if answer * i > LIMIT:
        break

print("answer: {0}".format(answer))
