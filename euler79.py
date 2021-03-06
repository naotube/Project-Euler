if __name__ == "__main__":

    with open('problem_euler79.txt', encoding='utf-8') as file:
        numbers = list(file)
        numbers = [number.rstrip() for number in numbers]
        numbers = list(set(numbers))
        digits = list(set("".join(numbers)))
        passcode = []
        while len(numbers) > 0:
            for d in digits:
                isMostLeft = True
                for number in numbers:
                    if d in number:
                        if not number.index(d) == 0:
                            isMostLeft = False
                if isMostLeft:
                    passcode.append(d)
                    numbers = [number[1:] if number[0] == d else number for number in numbers]
                    while '' in numbers:
                        numbers.remove('')
                    if all(d not in number for number in numbers):
                        digits.remove(d)
        print("".join(passcode))
