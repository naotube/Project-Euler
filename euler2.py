list=[2]
x = 1
y = 2
i = x + y
while i < 4000000:
    if i % 2 == 0:
        list.append(i)
    x = y
    y = i
    i = x + y

print(list)
print(sum(list))
