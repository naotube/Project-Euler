#! /usr/bin/env python
# By listing the first six prime numbers: 2, 3, 5, 7, 11, and 13,
# we can see that the 6th prime is 13.
# What is the 10001st prime number?

primes = [2,3]

def is_prime(num):
    """if num is a prime number, returns True, else returms False"""
    for i in primes:
        if num % i == 0:
            return False
    return True

def next_prime(num):
    """returns a first prime number larger than num"""
    while 1:
        num = num + 1
        if is_prime(num):
            return num

i = 2
while len(primes) < 10002:
    i = next_prime(i)
    primes.append(i)

print(primes[10000])
