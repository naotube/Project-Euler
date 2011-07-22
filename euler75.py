L = 1500000

one_ra_triangle = 0
for i in range(1,L+1):
    count = 0
    for c in range(i,0,-1):
        for a in range(1,i-c):
            b = i-c-a
            if a > b:
                break
            if c ** 2 == a ** 2 + b ** 2:
                count += 1
            if count > 1:
                break
        if count > 1:
            break
    if count == 1:
        one_ra_triangle += 1
        print(i, one_ra_triangle)
print("answer: {0}".format(one_ra_triangle))

