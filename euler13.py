with open('problem_euler13.txt', encoding='utf-8') as digit_list:
    print(str(sum([int(line) for line in digit_list]))[0:10])
