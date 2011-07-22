from itertools import combinations
from math import sqrt
LIMIT = 10 ** 3
sums_of_consecutive_squares = (sum(i ** 2 for i in range(1,n)) for n in range(1, int(sqrt(LIMIT))))
target_numbers = (n[1] - n[0] for n in combinations(sums_of_consecutive_squares, 2) if n[1] - n[0] < LIMIT and n[1] - n[0] == int(str(n[1] - n[0])[::-1]) and n[1] - n[0] not in (i ** 2 for i in range(1, int(sqrt(LIMIT)))))
answer = sum([n for n in target_numbers])
print(answer)

