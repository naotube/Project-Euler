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
                    digits.remove(d)
                    numbers = [number.replace(d, '') for number in numbers]
            if '' in numbers:
                numbers.remove('')
        print("".join(passcode))
