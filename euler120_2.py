TOP = 1000
sum_r_max = 0
for a in range(3, TOP + 1):
    if a % 2 == 0:
        r_max = a ** 2 - a * 2
    else:
        r_max = a ** 2 - a
    sum_r_max += r_max
print(sum_r_max)
