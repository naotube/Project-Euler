sum_of_squares = sum([i * i for i in range(1,101)])
sum_of_numbers = sum([i for i in range(1,101)])
square_of_sum = sum_of_numbers * sum_of_numbers
print(square_of_sum - sum_of_squares)
