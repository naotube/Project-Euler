#! /usr/bin/env python
# 2520 is the smallest number that can be divided by each of the numbers 
# from 1 to 10 without any remainder.
# What is the smallest positive number that is evenly divisible 
# by all of the numbers from 1 to 20?

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
    if num == 2:
        return 3
    while 1:
        num = num + 2
        if is_prime(num):
            return num

def factors(num):
    factors = []
    i = 2
    TARGET = num
    while i <= sqrt(TARGET):
        if num % i == 0:
            num = num / i
            factors.append(i)
        else:
            i = next_prime(i)
            if not i in primes:
                primes.append(i)
    if not num == 1:
        factors.append(int(num))
    return factors

list_of_factors = []
for i in range(3,21):
    list_of_factors.append(factors(i))

print(primes)
