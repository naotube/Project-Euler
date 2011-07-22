LIMIT = 10 ** 9
reversible = 0

for i in range(1, LIMIT):
    if not i % 10 == 0 and all(not int(d) % 2 == 0 for d in str(i + int(str(i)[::-1]))):
        reversible += 1
        print(i)
print("{0} reversible numbers exist below {1}".format(reversible, LIMIT))
