SPIRAL_LIMIT = 1001
number = 1
spiral_size = 1
count = 0
sum_of_diagonals = 0
while True:
    if count % 4 == 0:
        spiral_size = spiral_size + 2
    sum_of_diagonals = sum_of_diagonals + number
    number = number + (spiral_size - 1)
    count = count + 1
    if spiral_size > SPIRAL_LIMIT:
        break

print(sum_of_diagonals)
