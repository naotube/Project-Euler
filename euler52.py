if __name__ == "__main__":

    number = 1
    while True:
        if all(set(str(x * number)) == set(str(number)) for x in range(2,7)):
            break
        number += 1
    print(number)
