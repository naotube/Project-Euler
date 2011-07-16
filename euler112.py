from itertools import count

if __name__ == "__main__":
    increasing_number = 0
    decreasing_number = 0
    flat_number = 0
    bouncy_number = 0
    for i in count(1):
        increase = 0
        decrease = 0
        digits = [int(d) for d in str(i)]
        differences = [digits[i+1] - digits[i] for i in range(len(digits)-1)]
        if all(d == 0 for d in differences) or differences == []:
            flat_number += 1
        elif all(d >= 0 for d in differences):
            increasing_number += 1
        elif all(d <= 0 for d in differences):
            decreasing_number += 1
        else:
            bouncy_number += 1

        if bouncy_number / (increasing_number + decreasing_number + flat_number + bouncy_number) >= 0.99:
            answer = i
            break
    print("answer: {0}".format(answer))
