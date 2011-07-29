from itertools import count

def f(a, n):
    return (a - 1) ** n + (a + 1) ** n

TOP = 1000
sum_r_max = 0
for a in range(3, TOP + 1):
    r_max = 0
    r_appeared = set()
    for n in count(1, 2):
        r = f(a, n) % (a ** 2)
        if r > r_max:
            r_max = r
        if r in r_appeared:
            break
        r_appeared.add(r)
    sum_r_max += r_max
print(sum_r_max)
