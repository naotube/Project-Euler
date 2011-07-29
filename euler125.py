from itertools import combinations
from math import sqrt
LIMIT = 10 ** 8
sums_of_consecutive_squares = (sum(i ** 2 for i in range(n + 1)) for n in range(int(sqrt(LIMIT)) + 1))
sums_of_consecutive_squares = (p[1] - p[0] for p in combinations(sums_of_consecutive_squares, 2) if p[1] - p[0] < LIMIT and p[1] - p[0] not in (i ** 2 for i in range(0, int(sqrt(LIMIT)))))

target_numbers = (n for n in set(sums_of_consecutive_squares) if str(n) == str(n)[::-1])
answer = sum(target_numbers)
print(answer)

