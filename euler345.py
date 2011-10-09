from itertools import permutations

if __name__ == "__main__":
    with open('problem_euler345.txt', encoding='utf-8') as problem:
        matrix = []
        for line in problem:
            line = line.replace('\n','')
            line = line.split(" ")
            line = [int(x) for x in line if not x == '']
            matrix.append(line)

        indexes = permutations(range(len(matrix)))
        biggest_matrix_sum = 0
        for index in indexes:
            matrix_sum = 0
            for j in range(len(matrix)):
                matrix_sum += matrix[j][index[j]]
            if matrix_sum > biggest_matrix_sum:
                biggest_matrix_sum = matrix_sum
                print(biggest_matrix_sum, index)

        print(biggest_matrix_sum)

