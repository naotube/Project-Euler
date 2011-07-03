x = 1
y = 1
i = 2
while True:
    i = i + 1
    z = x + y
    if len(str(z)) > 999:
        break
    x = y
    y = z

print(i)
