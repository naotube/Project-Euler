for a in range(1,999):
    for b in range(1,999):
        c = 1000 - a - b
        if a*a + b*b == c*c:
            print("{0}:{1}:{2}".format(a,b,c))
            print(a*b*c)
