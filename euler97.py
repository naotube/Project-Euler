number = 28433
for i in range(7830457):
    number = number * 2
    if number > 9999999999:
        number = int(str(number)[-10:])
number = number + 1
print(number)
