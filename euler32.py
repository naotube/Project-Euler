if __name__ == "__main__":
    numbers = [p*q for p in range(1,100) for q in range(100,10000) if all((str(p) + str(q) + str(p*q)).count(str(d)) == 1 for d in range(1,10)) and '0' not in (str(p) + str(q) + str(p*q))]
    print(sum(set(numbers)))
