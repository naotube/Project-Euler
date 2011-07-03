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
    """
    if not type(list).__name__ == 'list':
        return False
    for i in range(0,len(list)):
        if not len(list[i]) == i + 1:
            return False
    return True

def left(triangle):
    """
    choose left number of a line below,
    and make a new list for a triangle(one level smaller), top of that is the chosen number.
    >>> left([[1],[222,333],[44,66,55]])
    [[222], [44, 66]]
    >>> left([[1],[222,333],[44,66,55],[7,8,9,10]])
    [[222], [44, 66], [7, 8, 9]]
    """
    left = []
    for i in range(1,len(triangle)):
        left.append(triangle[i][:-1])
    return left

def right(triangle):
    """
    choose right number of a line below,
    and make a new list for a triangle(one level smaller), top of that is the chosen number.
    >>> right([[1],[222,333],[44,66,55]])
    [[333], [66, 55]]
    >>> right([[1],[222,333],[44,66,55],[7,8,9,10]])
    [[333], [66, 55], [8, 9, 10]]
    """
    right = []
    for i in range(1,len(triangle)):
        right.append(triangle[i][1:])
    return right

def max_triangle(triangle):
    """
    returns max value of sum of numbers on routes from top to bottom line of a triangle
    >>> max_triangle([[157]])
    157
    >>> max_triangle([[1],[221,37]])
    222
    >>> max_triangle([[1],[22,33],[444,666,555]])
    700
    >>> max_triangle([[1],[22,33,44],[666,555,777]])
    False
    """
    if not is_triangle(triangle):
        return False
    if len(triangle) == 1:
        return triangle[0][0]
    else:
        top_number = triangle[0][0]
        left_triangle  = max_triangle(left(triangle))
        right_triangle = max_triangle(right(triangle))
        if left_triangle > right_triangle:
            return top_number + left_triangle
        else:
            return top_number + right_triangle

if __name__ == "__main__":
    import doctest
    doctest.testmod()

    with open('problem_euler18.txt', encoding='utf-8') as file:
        triangle=[]
        for line in file:
            line = line.replace('\n','')
            line = line.split(" ")
            line = [int(x) for x in line]
            triangle.append(line)
        print(max_triangle(triangle))

