from itertools import count

def absolute_value(number):
    if number < 0:
        return -number
    return number

if __name__ == "__main__":
    n_digit_nth_power = 0
    for i in range(1,10):
        previous_distance = 255
        for n in count(1):
            length = len(str(i ** n))
            if length == n:
                n_digit_nth_power += 1
            distance = absolute_value(length - n)
            if previous_distance - distance < 0:
                break
            previous_distance = distance
    print("answer: {0}".format(n_digit_nth_power))
