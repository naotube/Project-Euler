limit = 100

def factorial(n):
    """docstring for factorial"""
    x = 1
    while True:
        x = x * n
        n = n - 1
        if n < 1:
            return x

print(sum([int(s) for s in str(factorial(limit))]))
