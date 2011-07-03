#! /usr/bin/env python
# The prime factors of 13195 are 5, 7, 13 and 29.
# What is the largest prime factor of the number 600851475143 ?

from math import sqrt

factor = 2
factors = []

TARGET = 600851475143

primes = [2,3]

def is_prime(num):
    """if num is a prime number, returns True, else returms False"""
    for i in primes:
        if num % i == 0:
            return False
    return True

def next_prime(num):
    """returns a first prime number larger than num"""
    while num < TARGET:
        num = num + 1
        if is_prime(num):
            return num

while factor < sqrt(TARGET):
    if TARGET % factor == 0:
        TARGET = TARGET / factor
        factors.append(factor)
    else:
        factor = next_prime(factor)
        primes.append(factor)
factors.append(TARGET)

print(factors[-1])
