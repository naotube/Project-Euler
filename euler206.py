from math import sqrt,ceil,floor
import re

if __name__ == "__main__":
    pattern = r'1\d2\d3\d4\d5\d6\d7\d8\d9\d0'
    for i in range(floor(sqrt(1020304050607080900)), ceil(sqrt(1929394959697989990)), 10):
        if re.match(pattern, str(i ** 2)):
            answer = i
            break
    print("answer: {0}".format(answer))
