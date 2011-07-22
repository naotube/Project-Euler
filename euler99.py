from math import log

with open('problem_euler99.txt', encoding='utf-8') as base_exp:
    numbers = base_exp.read()
    numbers = numbers.split("\n")
    numbers = [[int(m) for m in n.split(",")] for n in numbers]
    numbers = [n[1] * log(n[0]) for n in numbers]
    print("answer: {0}".format(numbers.index(max(numbers)) + 1))
