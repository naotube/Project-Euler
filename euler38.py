number = max([i for i in range(9000,10000) if all( (str(i) + str(i*2)).count(str(s)) == 1 for s in range(1,10))])
answer = int(str(number) + str(number * 2))
print(answer)
