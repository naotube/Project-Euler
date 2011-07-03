#! /usr/bin/env python
# The sum of the primes below 10 is 2 + 3 + 5 + 7 = 17.
# Find the sum of all the primes below two million.

from math import sqrt

primes = [2,3]

def is_prime(num):
    """if num is a prime number, returns True, else returms False"""
    for i in primes:
        if i > sqrt(num):
            break
        if num % i == 0:
            return False
    return True

def next_prime(num):
    """returns a first prime number larger than num"""
    while 1:
        num = num + 2
        if is_prime(num):
            return num

i = 3
while True:
    i = next_prime(i)
    if i > 2000000:
        break
    print(i)
    primes.append(i)

print(sum(primes))
