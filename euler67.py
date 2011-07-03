MAX_OF_TERM = 99
MIN_OF_TERM = 0

def is_triangle(list):
    """
    returns True if the list is triangle, and returns False if not.
    >>> is_triangle([[1],[23,56],[97,0,12]])
    True
    >>> is_triangle([[1],[16,53],[91,8,14],[22,567,23,1]])
    True
    >>> is_triangle([[1],[2,37,5],[22,54,88]])
    False
    >>> is_triangle(2)
    False
    >>> is_triangle('neko')
    False
    >>> is_triangle([123])
    False
    """
    if not type(list).__name__ == 'list':
        return False
    if not type(list[0]).__name__ == 'list':
        return False
    for i in range(0,len(list)):
        if not len(list[i]) == i + 1:
            return False
    return True

def max_of_sums(list):
    """returns max number in the list of sums
    >>> max_of_sums([[0, 222], [1, 34], [1, 2455], [21, 23]])
    2455
    """
    numbers = []
    for i in range(len(list)):
        numbers.append(list[i][1])
    return max(numbers)

def max_triangle(triangle):
    """
    returns max value of sum of numbers on routes from top to bottom line of a triangle
    >>> max_triangle([[157]])
    157
    >>> max_triangle([[1],[221,37]])
    222
    >>> max_triangle([[1],[22,33],[444,666,555]])
    700
    >>> max_triangle([[1],[22,9999],[444,666,555]])
    10666
    >>> max_triangle([[1],[22,33,44],[666,555,777]])
    False
    """
    if not is_triangle(triangle):
        return False
    else:
        sums = []
        sums.append(triangle[0])
        sums[0].insert(0,0)
        for i in range(1,len(triangle)):
            new_line_sums = []
            for j in range(len(sums)):
                index = sums[j][0]
                number = sums[j][1]
                new_line_sums.append([index, number + triangle[i][index]])
                new_line_sums.append([index+1, number + triangle[i][index+1]])

            sums_filtered = []
            for p in range(len(new_line_sums)):
                index = new_line_sums[p][0]
                number = new_line_sums[p][1]
                flagAppend = True
                for q in range(len(sums_filtered)):
                    if sums_filtered[q][0] == index:
                        flagAppend = False
                        if sums_filtered[q][1] < number:
                            sums_filtered.insert(q, new_line_sums[p])
                            sums_filtered.remove(sums_filtered[q+1])
                if flagAppend == True:
                    sums_filtered.append(new_line_sums[p])

            new_sums = []
            limit = max_of_sums(sums_filtered) - (MAX_OF_TERM * (len(triangle) -1 - i))
            for p in range(len(sums_filtered)):
                if not sums_filtered[p][1] < limit:
                    new_sums.append(sums_filtered[p])
            sums = new_sums
        return max_of_sums(sums)

if __name__ == "__main__":
    import doctest
    doctest.testmod()

    import time
    time_start = time.time()
    with open('problem_euler67.txt', encoding='utf-8') as file:
        triangle=[]
        for line in file:
            line = line.replace('\n','')
            line = line.split(" ")
            line = [int(x) for x in line]
            triangle.append(line)
        print(max_triangle(triangle))
    time_end = time.time()
    print(time_end-time_start)
